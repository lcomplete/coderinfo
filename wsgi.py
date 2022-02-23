#!/usr/bin/env python
# coding: utf-8

import os
import sys

sys.path.append(os.path.dirname(__file__))

activate_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'venv/bin/activate_this.py'))
activate_this = os.path.expanduser(activate_path)

execfile(activate_this, dict(__file__=activate_this))

from cinfo.app import create_app

settings = os.path.abspath(os.path.join(os.path.dirname(__file__), 'etc/settings.py'))
if os.path.exists(settings):
    os.environ['CINFO_SETTINGS'] = settings

application=create_app()