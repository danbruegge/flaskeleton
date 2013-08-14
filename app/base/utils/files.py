# -*- coding: utf-8 -*-


def ensure_dir(path):
    """Check if a dir exists and if not, create it.
    """
    import os

    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)
