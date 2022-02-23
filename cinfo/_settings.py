#!/usr/bin/env python
# coding: utf-8

DEBUG = False
TESTING = False
VERIFY_EMAIL = True
VERIFY_USER = True

#: site
SITE_TITLE = u'程序猿信息盒子'
SITE_URL = 'http://rssletter.xyz'
SITE_STYLES = ['/static/css/bootstrap.min.css',
               '/static/css/bootstrap-theme.min.css',
               '/static/css/site.css']
SITE_SCRIPTS = ['/static/js/jquery-1.7.2.min.js',
                '/static/js/bootstrap.min.js']

#: session
SESSION_COOKIE_NAME = 'ci_sess'
#SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

#: account
SECRET_KEY = 'secret key'
PASSWORD_SECRET = 'password secret'

#: sqlalchemy
# SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/dbname'
# SQLALCHEMY_POOL_SIZE = 100
# SQLALCHEMY_POOL_TIMEOUT = 10
# SQLALCHEMY_POOL_RECYCEL = 3600

#: cache settings
# find options on http://pythonhosted.org/Flask-Cache/
# CACHE_TYPE = 'simple'