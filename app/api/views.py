# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, jsonify
from flask import current_app as app
from app import dropbox
from app.base.utils import ensure_dir


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def auth():
    return u'Click <a href="%s">here</a> to login with Dropbox.'\
           % dropbox.login_url


@bp.route('/db/')
def db():
    if not dropbox.is_authenticated:
        return redirect(url_for('.auth'))

    items = dropbox.client.metadata('/marc-images/Portfolio 1/')

    get_dropbox_files(items)

    return jsonify(items=items)


def create_dropbox_file(path):
    """Create a file from dropbox
    """
    print path
    out = open(path, 'w')
    f = dropbox.client.get_file(path)
    out.write(f.read())


def get_dropbox_files(items):
    for item in items['contents']:
        # backslash is needed to create the folders
        path = '%s%s' % (app.config['MEDIA_ROOT'], item['path'])

        ensure_dir(path)

        # if current item is a folder
        if item['is_dir']:
            path += '/'

            subs = dropbox.client.metadata(path)
            print subs
            get_dropbox_files(subs)
        else:
            create_dropbox_file(path)
