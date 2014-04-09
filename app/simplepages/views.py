# -*- coding: utf-8 -*-
from flask import Blueprint, abort, render_template, current_app
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

bp = Blueprint(
    'simplepages',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/', defaults={'slug': 'default'})
@bp.route('/<slug>')
@login_required
def index(slug):
    try:
        return render_template('simplepages/{0}.html'.format(slug))
    except TemplateNotFound, e:
        current_app.logger.error(e)
        abort(404)
