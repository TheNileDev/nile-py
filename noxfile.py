from pathlib import Path

import nox

OPENAPI_URL = "https://prod.thenile.dev/openapi.yaml"


ROOT = Path(__file__).parent
API_ADDONS = ROOT / "api_addons"
# The API directory is also hardcoded in openapi-generator-config.yml,
#   so if you change this, change that too.
API_DIR = ROOT / "nile_api"
OPENAPI_PATH = ROOT / "spec/api.yaml"
GENERATE_REQUIREMENTS = ROOT / "openapi-generator-requirements"
GENERATE_CONFIG = ROOT / "openapi-generator-config.yml"
TESTS = ROOT / "tests/"
TEMPLATES = ROOT / "templates"

nox.options.sessions = []


def session(default=True, **kwargs):
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(**kwargs)(fn)

    return _session


@session(python=["3.7", "3.8", "3.9", "3.10", "pypy3"])
def tests(session):
    session.install("pytest")
    # needed for importing events module
    session.install("httpx")
    session.install("python-dateutil")
    session.run("pytest", "-s", str(TESTS))


@session(tags=["build"])
def build(session):
    session.install("build")
    tmpdir = session.create_tmp()
    session.run("python", "-m", "build", str(ROOT), "--outdir", tmpdir)


@session(tags=["style"])
def readme(session):
    session.install("build", "twine")
    tmpdir = session.create_tmp()
    session.run("python", "-m", "build", str(ROOT), "--outdir", tmpdir)
    session.run("python", "-m", "twine", "check", tmpdir + "/*")


@session(default=False)
def update_openapi_requirements(session):
    session.install("pip-tools")
    session.run("pip-compile", "-U", "-r", f"{GENERATE_REQUIREMENTS}.in")


@session(default=False)
def regenerate(session):
    session.install("-r", f"{GENERATE_REQUIREMENTS}.txt")
    # See openapi-generators/openapi-python-client#684
    with session.chdir(ROOT.parent):
        session.run("curl", OPENAPI_URL, "-o", str(OPENAPI_PATH))
        # Temp hack until THE-831 is fixed and deployed to prod
        session.run(
            "sed",
            "-I",
            ".bak",
            "s#'\\*/\\*'#application/json#",
            str(OPENAPI_PATH),
        )
        session.run(
            "openapi-python-client",
            "update",
            "--path",
            str(OPENAPI_PATH),
            "--config",
            str(GENERATE_CONFIG),  # str() until wntrblm/nox#649 is released
            "--custom-template-path",
            str(TEMPLATES),
        )
        # We need to run cp because openapi-python-client doesn't support
        # ignoring files and just deletes everything in API_DIR when generating.
        session.run("cp", "-a", str(API_ADDONS) + "/.", str(API_DIR) + "/")
