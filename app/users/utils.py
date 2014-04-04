# -*- coding: utf-8 -*-
import hashlib

from app.users.models import User


def init_users(app):
    """Function doc
    """

    USER_LIST = app.config['USER_LIST']

    for user in USER_LIST:
        app.config['USERS'][user] = User(user, USER_LIST[user], user)


def sha512(value):
    """Function doc
    """

    return hashlib.sha512(value).hexdigest()
