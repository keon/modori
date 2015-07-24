#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#import sys
#import subprocess
#from flask_script import Manager, Shell, Server

from modori.app import create_app
from modori.settings import DevConfig, ProdConfig

if os.environ.get("modori_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

#HERE = os.path.abspath(os.path.dirname(__file__))
#TEST_PATH = os.path.join(HERE, 'tests')

#app = Flask(app)

#def _make_context():
#    """Return context dict for a shell session so you can access
#    app, db, and the User model by default.
#    """
#    return {'app': app, 'db': db, 'User': User}

#@manager.command
#def test():
#    """Run the tests."""
#    import pytest
#    exit_code = pytest.main([TEST_PATH, '--verbose'])
#    return exit_code
#
#manager.add_command('server', Server())
#manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
