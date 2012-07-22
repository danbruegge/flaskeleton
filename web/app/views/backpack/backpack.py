# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app

bp = Blueprint(
    'backpack',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/admin/'
)

#~ view functions
def list_blueprints():
    context = {}

    return render_template('admin/index.html', **context)

#~ define urls
bp.add_url_rule('', view_func=list_blueprints)