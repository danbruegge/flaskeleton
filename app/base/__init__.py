# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint(
    'base',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route('/base')
def base():
    print dir(bp)
    print bp.static_folder
    print bp.static_url_path

    return 'hello world'
