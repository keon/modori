# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask, render_template

from modori.settings import ProdConfig
from modori.extensions import (
    bcrypt,
    api,
)
from modori import route


def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    api.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(route.api.mod)
    return None

