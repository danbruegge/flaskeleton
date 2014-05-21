# -*- coding: utf-8 -*-
from werkzeug.securityy import generate_password_hash, check_password_hash
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

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password)

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.name, key='deterministic')
