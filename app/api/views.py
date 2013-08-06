# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from app import dropbox

bp = Blueprint(
    'api',
    __name__,
    url_prefix = '/api'
)

@bp.route('/')
def auth():
    return u'Click <a href="%s">here</a> to login with Dropbox.'\
           % dropbox.login_url


@bp.route('/db/')
def db():
    if not dropbox.is_authenticated:
        return redirect(url_for('home'))

    items = dropbox.client.metadata('/Kamera-Uploads')

    return jsonify(items=items)
