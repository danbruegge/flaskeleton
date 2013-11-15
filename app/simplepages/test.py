# -*- coding: utf-8 -*-
import os
import unittest
import flask

from views import bp


class SimplepagesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask(__name__)
        self.app.register_blueprint(bp)
        self.appTC = self.app.test_client()

    def tearDown(self):
        pass

    def test_show(self):
        r = self.appTC.get('/info')
        print r.data
        assert '404 Not Found' in r.data


if __name__ == '__main__':
    unittest.main()
