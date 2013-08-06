from fabric.api import env, local, run


def live():
    env.hosts = ['dronf.net']
    env.user = 'deadshox'
    env.cwd = 'web/<project>/project'


def git_pull():
    run('git pull')


def pip_install():
    command = 'pip install -U -r requirements.txt'

    if env.host:
        run(command)
    else:
        local(command)


def pip_update():
    command = 'pip freeze --local | grep -v "^\-e" | cut -d = -f 1  | '\
              'xargs pip install -U'

    if env.host:
        run(command)
    else:
        local(command)


def pip_requirements():
    command = 'pip freeze > requirements.txt'

    if env.host:
        run(command)
    else:
        local(command)


def compile():
    local('lessc -x --verbose'
          ' app/static/project/less/style.less'
          ' app/static/project/css/compiled.css')


def activate():
    run('. ../bin/activate')


def deactivate():
    run('deactivate')


def touch():
    run('touch app.wsgi')


def update():
    git_pull()
    touch()


def full_update():
    git_pull()
    activate()
    pip_install()
    deactivate()
    touch()
