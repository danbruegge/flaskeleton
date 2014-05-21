# -*- coding: utf-8 -*-
from app.settings import *


SECRET_KEY = ''
DEBUG = True
ASSETS_DEBUG = DEBUG

DEBUG_TB_PROFILER_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Users app
# TODO: redundant if users app uses a database
if 'users' in BLUEPRINTS:
    from app.users.models import User

    USERS = {
        'admin': User(
            'admin',
            'password please secure me',
            1
        )
    }
