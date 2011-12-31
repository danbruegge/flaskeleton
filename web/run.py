#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Brüggemann'
__version__ = '0.next'
__license__ = '-.-'

from app import create_app, settings

#------------------------------------------------------------------------------
if __name__ == '__main__':
    app = create_app(settings.Development)
    app.run(host='localhost', port=8080)
