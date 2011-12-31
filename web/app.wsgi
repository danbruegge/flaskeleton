import sys, os

activate_this = '/.../bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path = [os.path.dirname(__file__)] + sys.path
os.chdir(os.path.dirname(__file__))

sys.stdout = sys.stderr

from app import create_app, settings
application = create_app(settings.Production)