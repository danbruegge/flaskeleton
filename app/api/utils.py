# -*- coding: utf-8 -*-
from flask import current_app as app
from app.base.utils import ensure_dir


def create_dropbox_file(client, local_path, path):
    """Save file from dropbox to local path
    """

    with open(local_path, 'wb') as f:
        data = client.get_file(path)
        f.write(data.read())


def get_dropbox_files(client, path):
    """Recursive function to get all files from dropbox folder
    """

    data = client.metadata(path)

    for item in data['contents']:
        # backslash is needed to create the folders
        local_path = '%s%s' % (app.config['MEDIA_ROOT'], item['path'])

        ensure_dir(local_path)

        # if current item is a folder
        if item['is_dir']:
            get_dropbox_files(client, '%s/' % item['path'])
        else:
            create_dropbox_file(client, local_path, item['path'])
