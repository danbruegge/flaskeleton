# -*- coding: utf-8 -*-

def add_blueprints(app):
    from werkzeug.utils import import_string

    for module in app.config['BLUEPRINTS']:
        bp = import_string('app.views.' + module + '.bp')
        app.register_blueprint(bp)