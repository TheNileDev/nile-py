======================
Nile API Python Client
======================

This is the Python SDK for interacting with `Nile <https://thenile.dev>`_.

Installing
----------

The Nile Python SDK is available on `PyPI <https://pypi.org/project/nile-api/>`_, and can be installed via:

.. code-block:: sh

    pip install nile-api

(in a virtual environment as appropriate).

Usage
-----

Usage examples of the SDK can be found in the Nile `examples repository <https://github.com/TheNileDev/examples/>`_, within the directories with ``-python`` in their name.

Basic Example:
-----

.. code-block:: python

    import os

    from nile_api import AuthenticatedClient
    from nile_api.api.users import create_user, list_users
    from nile_api.models.create_user_request import CreateUserRequest

    # Create an authenticated client with a workspace auth token
    client = AuthenticatedClient(base_url='https://prod.thenile.dev', token=os.environ.get("NILE_WS_TOKEN"))

    # Create a user
    user = create_user.sync(
                workspace=os.environ.get("NILE_WORKSPACE"),
                client=client,
                json_body=CreateUserRequest(email="anon@anon.com", password="secret"),
            )

    # Log created user to console
    print(user.email);

    # List all users in the workspace
    users = list_users.sync(client=client, workspace=os.environ.get("NILE_WORKSPACE"))
    for user in users:
        print(f"User {user.email!r} exists")


Development
-----------

Commands below generally make use of `nox <https://nox.thea.codes/en/stable/index.html#>`_ (in some sense a Python-based, testing-centric ``make``).

You can install it by following its `install instructions <https://nox.thea.codes/en/stable/index.html#welcome-to-nox>`_ for your OS, or e.g. on macOS, by simply running:

.. code-block:: sh

    brew install nox

Regenerating (updating) the client is done via `openapi-python-client <https://github.com/openapi-generators/openapi-python-client>`_.

To do so, run:

.. code-block:: sh

    nox -s regenerate

You will want to test the results. First, validate that the client generated with the expected structure (packages and modules):

To do so, run:

.. code-block:: sh

    nox -s tests
    
Then you'll want to do a quick smoke test and make sure the client actually works against Nile. 
Currently we do it by running https://github.com/TheNileDev/examples/tree/main/quickstart-python example.
Before running it you'll want to make sure that running the example will use the local client and not an installed one. 

From the local nile-py repository directory run:

.. code-block:: sh

    export PYTHONPATH=`pwd`:$PYTHONPATH
    venv/bin/python -c "import nile_api; print(str(nile_api.__path__))"
    cd ../examples/quickstart-python
    ./venv/bin/python src/all.py

We pin the version of this generator itself in a requirements file.
To update the version of the generator that will be used, run:

.. code-block:: sh

    nox -s update_openapi_requirements

which should regenerate the ``openapi-generator-requirements.txt`` file which you should then commit.
