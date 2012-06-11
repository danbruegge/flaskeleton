# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from urls import add_urls

bp = Blueprint('page', __name__, template_folder='templates')

# -----------------------------------------------------------------------------
# view functions
# -----------------------------------------------------------------------------
def show(page_slug):
    context = {}

    return 'SHOW'

def add():
    context = {}

    return render_template('pages/add.html', **context)

def edit(page_slug):
    context = {}

    return 'EDIT'

def delete(page_slug):
    context = {}

    return 'DEL'

# -----------------------------------------------------------------------------
# define urls
# -----------------------------------------------------------------------------
bp.add_url_rule('/admin/pages/delete/<page_slug>', methods=('GET', 'POST'), view_func=delete)
bp.add_url_rule('/admin/pages/<page_slug>', methods=('GET', 'POST'), view_func=edit)
bp.add_url_rule('/admin/pages/', methods=('GET', 'POST'), view_func=add)
bp.add_url_rule('/<page_slug>/', view_func=show)