from pathlib import Path

import nox

OPENAPI_URL = "https://prod.thenile.dev/openapi.yaml"

ROOT = Path(__file__).parent
GENERATE_REQUIREMENTS = ROOT / "openapi-generator-requirements"
GENERATE_CONFIG = ROOT / "openapi-generator-config.yml"

nox.options.sessions = []


def session(default=True, **kwargs):
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(**kwargs)(fn)

    return _session


@session(default=False)
def update_openapi_requirements(session):
    session.install("pip-tools")
    session.run("pip-compile", "-U", "-r", f"{GENERATE_REQUIREMENTS}.in")


@session(default=False)
def regenerate(session):
    session.install("-r", f"{GENERATE_REQUIREMENTS}.txt")
    # See openapi-generators/openapi-python-client#684
    with session.chdir(ROOT.parent):
        session.run(
            "openapi-python-client",
            "update",
            "--url",
            OPENAPI_URL,
            "--config",
            str(GENERATE_CONFIG),  # str() until wntrblm/nox#649 is released
        )
