# -*- coding: utf-8 -*-
from flask import current_app
from flask.ext.login import login_user
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length

from app.users.utils import sha512


class LoginForm(Form):
    username = TextField('Username', validators=[
        DataRequired(),
        Length(min=4, max=35)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, max=35)
    ])

    def validate_username(form, field):
        users = current_app.config['USERS']

        if field.data not in users:
            raise ValidationError('Username not found')

    def validate_password(form, field):
        if form.username.errors:
            return False

        username = form.username.data
        password = sha512(field.data)
        user = current_app.config['USERS'][username]

        if not password == user.get_password():
            raise ValidationError('Incorrect password')
