# -*- coding: utf-8 -*-
import sys
import os
import unittest

sys.path = [os.path.abspath('')] + sys.path

from app.test import BaseTestCase


class SimplepagesTestCase(BaseTestCase):
    def test_show(self):
        error_msg = '404 - Seite nicht gefunden / Page not found'
        page = self.test_client.get('/')
        assert error_msg not in page.data
        page = self.test_client.get('/info')
        assert error_msg not in page.data


if __name__ == '__main__':
    unittest.main()
