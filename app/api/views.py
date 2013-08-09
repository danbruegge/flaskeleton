# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, jsonify
from app import dropbox
from app.api.utils import get_dropbox_files


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/', methods=['GET'])
def auth():
    if not dropbox.is_authenticated:
        return u'Click <a href="%s">here</a> to login with Dropbox.'\
               % dropbox.login_url

    return 'Logged in! View json: <a href="%s">here</a>!' % url_for('.db')


@bp.route('/db/')
def db():
    if not dropbox.is_authenticated:
        return redirect(url_for('.auth'))

    get_dropbox_files(dropbox.client, '/marc-images')

    return jsonify(items={})
