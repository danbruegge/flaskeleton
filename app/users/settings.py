# -*- coding: utf-8 -*-
from app.users.models import User


USERS_BASE_TPL = 'base.html'

# TODO: this dict should be redundant if the users app will use a database
USERS = {
    'admin': User(  # usersname
        'admin',  # usersname
        'admin123',  # password
        1  # id
    )
}

USERS_CURRENT = None

USERS_REDIRECT_LOGIN = 'simplepages.index'
USERS_REDIRECT_LOGOUT = 'simplepages.index'
