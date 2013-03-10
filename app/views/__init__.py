# -*- coding: utf-8 -*-
from werkzeug.utils import import_string, ImportStringError

def add_blueprints(app):
    for module in app.config['BLUEPRINTS']:
        bp = import_string('app.views.' + module + '.bp')
        app.register_blueprint(bp)

        try:
            admin = import_string('app.views.' + module + '.admin')
            app.register_blueprint(admin)
        except ImportStringError:
            print module + ' has no admin blueprint.'

    return app