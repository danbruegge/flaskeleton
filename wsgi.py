import sys, os

ROOT_PATH = '/<PATH>/bin/activate_this.py'
ENV_PATH = ROOT_PATH + '/bin/activate_this.py'
WSGI_PATH = ROOT_PATH + '/project'

activate_this = ENV_PATH
execfile(activate_this, dict(__file__=activate_this))

if WSGI_PATH not in sys.path:
    sys.path = [WSGI_PATH] + sys.path

os.chdir(os.path.dirname(__file__))

sys.stdout = sys.stderr

from app import create_app
application = create_app('production.py')
