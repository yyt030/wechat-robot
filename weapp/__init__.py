#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

from sanic import Sanic
from sanic.exceptions import NotFound, ServerError

from config import config


def create_app(config_name):
    app = Sanic(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # blueprint
    register_blueprint(app)

    # error handle
    # register_error_handle(app)
    return app


def register_error_handle(app):
    @app.exception([NotFound])
    def ignore_404(request, exception):
        # return text("Yep, I totally found the page: {}".format(request.url))
        pass

    @app.exception(ServerError)
    def ignore_500(request, exception):
        # return 505
        pass

    pass


def register_blueprint(app):
    from weapp.controller import main
    app.register_blueprint(main.bp, url_prefix='/')
    pass
