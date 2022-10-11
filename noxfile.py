from pathlib import Path
import nox

OPENAPI_URL = "https://prod.thenile.dev/openapi.yaml"

ROOT = Path(__file__).parent
GENERATE_REQUIREMENTS = ROOT / "openapi-generator-requirements"

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
