# -*- coding: utf-8 -*-
import os


def ensure_dir(path):
    """Check if a dir exists and if not, create it."""
    import os

    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)


def extend_filename(filename, extend):
    """Extend a filename at the end but before the extension."""
    # split image path in path and image name
    path, name = os.path.split(filename)

    # add name addition
    name = name.replace('.', '%s.' % extend)

    # put all together and return
    return os.path.join(path, name)
