from fabric.api import *


def pip_update():
    local('pip freeze --local | grep -v "^\-e" | cut -d = -f 1  | xargs pip install -U')


def pip_requirements():
    local('pip freeze > requirements.txt')
