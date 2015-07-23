===============================
MODORI
===============================

description here


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export kaizen_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/kwk236/kaizen
    cd kaizen
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.




Deployment
----------

In your production environment, make sure the ``FLASK_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``.


Running Tests
-------------

To run all tests, run ::

    python manage.py test
