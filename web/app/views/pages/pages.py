# -*- coding: utf-8 -*-

import datetime
from werkzeug.datastructures import ImmutableMultiDict
from flask import g, Blueprint, render_template
from settings import PAGES
from forms import PageForm

bp = Blueprint('pages', __name__, template_folder='templates')

# =============================================================================
# view functions
# =============================================================================
def show(page_slug):
    context = {}

    return 'SHOW'

def add():
    context = {}
    context['form'] = form = PageForm()
    form.author.data = 'Ich'

    if form.validate_on_submit():
        pages = g.db.db.pages
        result = pages.insert(form.data)

        context['success'] = True

    return render_template('pages/add.html', **context)

def edit(page_slug):
    context = {}
    context['page'] = page = g.db.db.pages.find_one_or_404({'slug': page_slug})

    print page

    context['form'] = form = PageForm(ImmutableMultiDict(page))

    if form.validate_on_submit():
        result = page.update(form.data)

        context['success'] = True

    return render_template('pages/edit.html', **context)

def delete(page_slug):
    context = {}

    return 'DEL'

# =============================================================================
# define urls
# =============================================================================
bp.add_url_rule(PAGES['prefix'] + 'delete/<page_slug>/', methods=('GET', 'POST'), view_func=delete)
bp.add_url_rule(PAGES['prefix'] + '<page_slug>/', methods=('GET', 'POST'), view_func=   edit)
bp.add_url_rule(PAGES['prefix'], methods=('GET', 'POST'), view_func=add)
bp.add_url_rule('/<page_slug>/', view_func=show)
