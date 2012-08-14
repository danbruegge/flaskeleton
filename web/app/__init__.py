# -*- coding: utf-8 -*-

from flask import Flask, g, send_file, render_template
from flask.ext.assets import Environment, Bundle
from flask.ext.pymongo import PyMongo
from app import settings

assets = Environment()
mongo = PyMongo()

def create_app(config_object):
    app = Flask(
        __name__
    )
    app.config.from_object(config_object)

    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler(
            app.config['ERROR_MAIL']['smtp'],
            app.config['ERROR_MAIL']['to'],
            app.config['ERROR_MAIL']['from'],
            app.config['ERROR_MAIL']['subject']
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    mongo.init_app(app)
    @app.before_request
    def connect_db():
        g.db = mongo

    assets.init_app(app)

    from app.views import add_blueprints
    app = add_blueprints(app)

    @app.before_request
    def get_admin_prints():
        g.admin_blueprints = [key for key in app.blueprints if 'admin_' in key]

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', **{'title':'Seite nicht gefunden'})

    app.add_url_rule('/<path:filename>', endpoint='static', view_func=app.send_static_file)
    app.add_url_rule('/media/<path:filename>', endpoint='media', view_func=send_file)

    return app