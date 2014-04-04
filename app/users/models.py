# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin, make_secure_token


class User(UserMixin):
    password = ''

    def __init__(self, name, password, id, active=True):
        self.id = id
        self.name = name
        self.password = password
        self.active = active

    def get_id(self):
        return self.id

    def get_password(self):
        return self.password

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.name, key='deterministic')
