======================
Nile API Python Client
======================

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

We pin the version of this generator itself in a requirements file.
To update the version of the generator that will be used, run:

.. code-block:: sh

    nox -s update_openapi_requirements

which should regenerate the ``openapi-generator-requirements.txt`` file which you should then commit.
