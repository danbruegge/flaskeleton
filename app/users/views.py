# -*- coding: utf-8 -*-
from flask import (Blueprint, request, redirect, url_for, render_template,
                   current_app)
from flask.ext.login import login_user, logout_user, login_required

from app import login_manager
from app.users.forms import LoginForm


bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='templates/'
)


@login_manager.user_loader
def load_user(user):
    try:
        return current_app.config['USERS'][user]
    except KeyError:
        return None


@bp.route('', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(current_app.config['CURRENT_USER'])

        return redirect(request.args.get('next') or url_for('index'))

    return render_template('users/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('admin.index'))
