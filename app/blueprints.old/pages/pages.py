# -*- coding: utf-8 -*-

from flask import g, Blueprint, render_template
from forms import PageForm

bp = Blueprint(
    'pages',
    __name__,
    template_folder='templates'
)

#~ view functions
def show(page_slug):
    context = {}
    context['page'] = g.db.db.pages.find_one_or_404({'slug': page_slug})

    return render_template('pages/show.html', **context)

#~ define urls
bp.add_url_rule('/<page_slug>/', view_func=show)