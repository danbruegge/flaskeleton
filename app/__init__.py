# -*- coding: utf-8 -*-
from flask import (Flask, g, request, send_file, send_from_directory,
                   render_template)
from flask.ext.assets import Environment
from flask.ext.login import current_user
from base.utils.core import (load_blueprint_settings, load_blueprints,
                             error_handler)


assets = Environment()


def create_app(settings):
    app = Flask(__name__)

    # load base settings at first
    app.config.from_pyfile('settings.py')

    # simple load all blueprint settings, enabled in settings
    load_blueprint_settings(app)

    # load development or production settings at last
    app.config.from_pyfile(settings)

    # Setup assets
    assets.init_app(app)

    # simple load all blueprints, enabled in settings
    load_blueprints(app)

    # Enable DebugToolbar on debug
    # Enable error handler on productive mode
    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)
    else:
        # add errorhandler
        error_handler(app)

    @app.before_request
    def before_request():
        g.user = current_user

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/robots.txt')
    @app.route('/favicon.ico')
    # @app.route('/sitemap.xml')
    # @app.route('/google-webmaster-tools-auth.html')
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    app.add_url_rule('/media/<path:filename>', endpoint='media',
                     view_func=send_file)

    return app
