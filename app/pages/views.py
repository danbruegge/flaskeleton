# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint(
    'pages',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/', defaults={'page': 'default'})
@bp.route('/<page>')
def show(page):
    return render_template('pages/%s.html' % page)
