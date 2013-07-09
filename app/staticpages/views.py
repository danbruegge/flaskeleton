# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint(
    'staticpages',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/grid')
def grid():
    return render_template('grid.html')


@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
def show(page):
    return render_template('staticpages/%s.html' % page)
