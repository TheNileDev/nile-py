======================
Nile API Python Client
======================

Development
-----------

Regenerating (updating) the client is done via `openapi-python-client <https://github.com/openapi-generators/openapi-python-client>`_.

We pin the version of this generator itself in a requirements file.
To update the version of the generator that will be used, run:

.. code-block:: sh

    nox -s update_openapi_requirements

which should regenerate the ``openapi-generator-requirements.txt`` file which you should then commit.
