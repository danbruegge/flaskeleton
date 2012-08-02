# -*- coding: utf-8 -*-

class Config():
    DEBUG = False
    ASSETS_DEBUG = DEBUG
    SECRET_KEY = '<secret_key>'

    USER = { '<user_name>': '<user_password>' }

    PAGE_DESCRIPTION = '<your description>'
    PAGE_OFFLINE = False
    PAGE_OFFLINE_MESSAGE = ''

    ERROR_MAIL = {
        'smtp': '<SMTP SERVER',
        'to': ['<TO>'],
        'from': '<FROM>',
        'subject': '<SUBJECT>'
    }

    BLUEPRINTS = ['backpack',]

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    ASSETS_DEBUG = DEBUG

    MONGO_HOST = '<HOST>'
    MONGO_PORT = 1234
    MONGO_DATABASE = '<DB>'
    MONGO_USERNAME = '<USER>'
    MONGO_PASSWORD = '<PASS>'