# -*- coding: utf-8 -*-
from flask import Blueprint, abort, render_template
from flask import current_app as app
from jinja2 import TemplateNotFound
from flask.ext.login import current_user

bp = Blueprint(
    'simplepages',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/', defaults={'slug': 'default'})
@bp.route('/<slug>')
def index(slug):
    page_login_required = slug in app.config['SIMPLEPAGES_LOGIN_REQUIRED']
    auth = not current_user.is_authenticated() 
    if auth and page_login_required:
        return app.login_manager.unauthorized()

    try:
        return render_template('simplepages/{0}.html'.format(slug))
    except TemplateNotFound, e:
        app.logger.error(e)
        abort(404)
