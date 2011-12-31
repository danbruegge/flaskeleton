# -*- coding: utf-8 -*-

from flask import Flask, g, send_file
from app import settings

db = null

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)

    @app.before_request
    def connect_db():
        g.db = db

    from app.views import install, pages
    app.register_blueprint(pages.bp)
    app.register_blueprint(install.bp)

    @app.route('/robots.txt')
    def robots_txt():
        return app.send_static_file('robots.txt')

    @app.route('/media/<path:filename>')
    def media(filename):
        return send_file('media/{0}'.format(filename))

    return app