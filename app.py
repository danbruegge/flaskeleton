#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app


if __name__ == '__main__':
    app = create_app('development.py')
    app.run(host='localhost', port=8000)
