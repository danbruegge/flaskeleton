# -*- coding: utf-8 -*-

class Config():
    DEBUG = False
    ASSETS_DEBUG = False
    SECRET_KEY = '...'

    ERROR_MAIL = {
        'smtp': '<SMTP SERVER>',
        'to': ['<TO>'],
        'from': '<FROM>',
        'title': 'Error on <PAGEAME>'
    }

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    ASSETS_DEBUG = True