#!/usr/bin/env python
# coding: utf-8

import os
from flask import Flask
from capture import capture_scheduler
from extensions import *


def create_app(config=None):
    app = Flask(__name__, template_folder='templates', static_folder='../static')
    app.config.from_pyfile('_settings.py')

    if 'CINFO_SETTINGS' in os.environ:
        app.config.from_envvar('CINFO_SETTINGS')

    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.config.from_pyfile(config)

    register_routes(app)
    configure_extensions(app)
    capture_scheduler.init_scheduler() # 初始化任务调度器
    return app


def configure_extensions(app):
    db.init_app(app)


def register_routes(app):
    from .views import home, pic
    app.register_blueprint(home.bp, url_prefix='')
    app.register_blueprint(pic.bp, url_prefix='/pic')
    return app
