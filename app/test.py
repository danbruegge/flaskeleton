# -*- coding: utf-8 -*-
import unittest

from app import create_app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development.py')
        self.test_client = self.app.test_client()
