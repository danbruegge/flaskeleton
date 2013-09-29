# -*- coding: utf-8 -*-
from flask import Flask, request, send_file, send_from_directory,\
    render_template
from flask.ext.assets import Environment
from base.utils.core import load_blueprints, error_handler


assets = Environment()


def create_app(settings):
    app = Flask(__name__)
    app.config.from_pyfile(settings)

    assets.init_app(app)

    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension(app)

    if not app.debug:
        error_handler(app)

    load_blueprints(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    @app.route('/robots.txt')
    # @app.route('/sitemap.xml')
    # @app.route('/google-webmaster-tools-auth.html')
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    app.add_url_rule('/media/<path:filename>', endpoint='media',
                     view_func=send_file)

    return app
