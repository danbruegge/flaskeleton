# -*- coding: utf-8 -*-
from flask import (Blueprint, request, redirect, url_for, render_template,
                   current_app)
from flask.ext.login import (LoginManager, login_user, logout_user,
                             login_required)

from app.users.forms import LoginForm


bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='templates/'
)

login_manager = LoginManager()


@bp.record_once
def on_load(state):
    # Setup LoginManager
    login_manager.init_app(state.app)
    login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(user_id):
    users = current_app.config['USERS']
    try:
        for username in users:
            if user_id == users[username].get_id():
                return users[username]
    except KeyError:
        return None


@bp.route('', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(current_app.config['USERS'][form.username.data])

        return (redirect(request.args.get('next')
                or url_for(current_app.config['USERS_REDIRECT_LOGIN'])))

    return render_template('users/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for(current_app.config['USERS_REDIRECT_LOGOUT']))
