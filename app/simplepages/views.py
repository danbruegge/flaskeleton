# -*- coding: utf-8 -*-
from flask import Blueprint, abort, render_template, current_app
from jinja2 import TemplateNotFound

bp = Blueprint(
    'simplepages',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/', defaults={'slug': 'default'})
@bp.route('/<slug>')
def show(slug):
    try:
        return render_template('simplepages/{0}.html'.format(slug))
    except TemplateNotFound:
        current_app.logger.error('404: Page "{0}" not found.'.format(slug))
        abort(404)
