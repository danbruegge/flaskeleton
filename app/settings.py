# -*- coding: utf-8 -*-
import os

BLUEPRINTS = ('pages', 'api',)

# Dropbox settings
DROPBOX_KEY = '37ar7pbvaltsl0u'
DROPBOX_SECRET = 'emlesfse8mrjzu0'
DROPBOX_ACCESS_TYPE = 'dropbox'
DROPBOX_CALLBACK_URL = '/api/'

# Upload stuff
MEDIA_ROOT = '%s/%s' % (os.path.dirname(__file__), '../../media')

# Site related
PAGE_DESCRIPTION = '<your description>'
USER = {'<user_name>': '<user_password>'}
