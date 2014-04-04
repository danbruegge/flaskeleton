# -*- coding: utf-8 -*-
import logging
from logging.handlers import SMTPHandler
from werkzeug.utils import import_string
# from werkzeug.utils import ImportStringError


def load_blueprints(app, blueprint_config='BLUEPRINTS',
                    blueprint_path='app', blueprint_name='bp'):
    """A simple blueprint loader, you only need to pass the app context and set
    a BLUEPRINTS constant with the a list of bluleprint names in the
    settings.py::

        BLUEPRINTS = ('blueprint1', 'blueprint2', )

    TODO: fix the admin stuff
    """

    for name in app.config[blueprint_config]:
        bp = import_string(
            '{0}.{1}.{2}'.format(blueprint_path, name, blueprint_name)
        )
        app.register_blueprint(bp)

        # load a settings file for the blueprint
        try:
            app.config.from_pyfile('{0}/settings.py'.format(name))
        except IOError:
            pass

        # try:
            # admin = import_string(
                # '{0}.{1}.{2}'.format(blueprint_path, name, 'admin')
            # )
            # app.register_blueprint(admin)
        # except ImportStringError:
            # print '%s has no admin blueprint.' % name

    return app


def error_handler(app):
    """Seperated to keep the `create_app()` clean.
        Onely pass the app context and set the rights variables::

        ERROR_MAIL = {
            'smtp': '<SMTP SERVER',
            'to': ['<TO>'],
            'from': '<FROM>',
            'subject': '<SUBJECT>'
        }
    """

    mail_handler = SMTPHandler(app.config['ERROR_MAIL']['smtp'],
                               app.config['ERROR_MAIL']['to'],
                               app.config['ERROR_MAIL']['from'],
                               app.config['ERROR_MAIL']['subject'])
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
