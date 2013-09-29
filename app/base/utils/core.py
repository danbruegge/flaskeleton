# -*- coding: utf-8 -*-


def load_blueprints(app, blueprint_config='BLUEPRINTS',
                    blueprint_path='app', blueprint_name='bp'):
    """A simple blueprint loader, you only need to pass the app context and set
    a BLUEPRINTS constant with the a list of bluleprint names in the
    settings.py::

        BLUEPRINTS = ['blueprint1', 'blueprint2', ]

    TODO: fix the admin stuff
    """
    from werkzeug.utils import import_string
    # from werkzeug.utils import import_string, ImportStringError

    try:
        for name in app.config[blueprint_config]:
            bp = import_string('%s.%s.%s' % (blueprint_path, name,
                                             blueprint_name))
            app.register_blueprint(bp)

            # try:
                # admin = import_string('%s.%s.%s'
                    # % (blueprint_path, name, 'admin'))
                # app.register_blueprint(admin)
            # except ImportStringError:
                # print '%s has no admin blueprint.' % name
    except KeyError:
        print 'No blueprints'

    return app


def error_handler(app):
    """Seperated to keep the `create_app()` clean.
    Only pass the app context and set the rights variables::

        ERROR_MAIL = {
            'smtp': '<SMTP SERVER',
            'to': ['<TO>'],
            'from': '<FROM>',
            'subject': '<SUBJECT>'
        }
    """
    from logging.handlers import SMTPHandler
    from logging import Formatter

    mail_handler = SMTPHandler(app.config['ERROR_MAIL']['smtp'],
                               app.config['ERROR_MAIL']['to'],
                               app.config['ERROR_MAIL']['from'],
                               app.config['ERROR_MAIL']['subject'])
    mail_handler.setFormatter(Formatter("""
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    """))
    app.logger.addHandler(mail_handler)
