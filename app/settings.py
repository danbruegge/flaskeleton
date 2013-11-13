# -*- coding: utf-8 -*-
import os

BLUEPRINTS = ('simplepages', )

# Upload stuff
MEDIA_ROOT = '{0}/{1}'.format(os.path.dirname(__file__), '../../media')

# Site related
PAGE_DESCRIPTION = '<your description>'
USER = {'<user_name>': '<user_password>'}
