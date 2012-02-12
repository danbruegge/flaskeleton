# -*- coding: utf-8 -*-

from flask import Flask, g, send_file, render_template
from flaskext.assets import Environment, Bundle
from app import settings

assets = Environment()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler(
            app.config['ERROR_MAIL']['smtp'],
            app.config['ERROR_MAIL']['to'],
            app.config['ERROR_MAIL']['from'],
            app.config['ERROR_MAIL']['title']
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    assets.init_app(app)

    @app.before_request
    def connect_db():
        g.db = db

    from app.views import install
    app.register_blueprint(install.bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', c={'title':'Seite nicht gefunden'})

    @app.route('/robots.txt')
    def robots_txt():
        return app.send_static_file('robots.txt')

    @app.route('/media/<path:filename>')
    def media(filename):
        return send_file('media/{0}'.format(filename))

    return app