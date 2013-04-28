# -*- coding: utf-8 -*-
from flask import Flask, send_file, render_template
from flask.ext.assets import Environment
from utils import load_blueprints, error_handler


def create_app(settings):
    app = Flask(__name__)
    app.config.from_pyfile(settings)

    assets = Environment(app)

    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension(app)

    if not app.debug:
        error_handler(app)

    load_blueprints(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    app.add_url_rule('/<path:filename>', endpoint='static',
                     view_func=app.send_static_file)
    app.add_url_rule('/media/<path:filename>', endpoint='media',
                     view_func=send_file)

    return app
