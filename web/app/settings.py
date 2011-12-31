# -*- coding: utf-8 -*-

class Config():
    DEBUG = False
    SECRET_KEY = '...'

class Production(Config):
    pass

class Development(Config):
    DEBUG = True