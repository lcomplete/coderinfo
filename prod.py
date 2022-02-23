#!/usr/bin/env python
# coding: utf-8

import os
from cinfo.app import create_app

settings = os.path.abspath('./etc/settings.py')
if not os.path.exists(settings):
    settings = os.path.abspath('./etc/settings.py')
if 'CINFO_SETTINGS' not in os.environ:
    os.environ['CINFO_SETTINGS'] = settings

app = create_app()

if __name__ == '__main__':
    app.run(use_reloader=False, port=80, host='0.0.0.0')
