# -*- coding: utf-8 -*-
from flask import Flask, g, send_file, render_template


def create_app(settings):
    app = Flask(__name__)
    app.config.from_pyfile(settings)

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

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', **{'title':'Seite nicht gefunden'})

    app.add_url_rule('/<path:filename>', endpoint='static', view_func=app.send_static_file)
    app.add_url_rule('/media/<path:filename>', endpoint='media', view_func=send_file)

    return app
