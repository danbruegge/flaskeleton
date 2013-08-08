# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, request, jsonify
from flask import current_app as app
from app import dropbox
from app.base.utils import ensure_dir


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

    items = dropbox.client.metadata('/marc-images')

    get_dropbox_files(items)

    return jsonify(items=items)


def create_dropbox_file(local_path, path):
    """Create a file from dropbox
    """
    with open(local_path, 'wb') as f:
        data = dropbox.client.get_file(path)
        f.write(data.read())


def get_dropbox_files(items):
    for item in items['contents']:
        # backslash is needed to create the folders
        local_path = '%s%s' % (app.config['MEDIA_ROOT'], item['path'])

        ensure_dir(local_path)

        # if current item is a folder
        if item['is_dir']:
            subs = dropbox.client.metadata('%s/' % item['path'])
            get_dropbox_files(subs)
        else:
            create_dropbox_file(local_path, item['path'])
