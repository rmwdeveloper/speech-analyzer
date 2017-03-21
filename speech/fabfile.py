###################################################################
#
# Deployment script for digital ocean servers
#
# Usage: fab <server> refresh
# <server> = dev, staging, prod
#
####################################################################
import os

from fabric.api import local, run, env, cd, prefix, sudo
from fabric.contrib.files import exists

def local():
    settings = 'speech.settings.settings'
    local('./manage.py migrate --settings={0}'.format(settings))


# def set_env():
#     env.venv = 'source /home/django/sites/{0}/env/bin/activate'.format(env.code_dir)
#     env.enviro = 'envdir /home/django/sites/{0}/src/academy/enviro/{1}'.format(env.code_dir, env.app_name)

ip = '0.0.0.0'
domain = 'talkr.pro'

env.hosts = [ip]
env.password = 'foo'
def tester():
    print('talkr.pro')
    env.hosts = [ip]
    env.user = 'tester'
    env.password = os.environ['DJANGO_USER_TEST'] #ssh password for user
    env.app_name = 'dev'
    # env.code_dir = 'rmw.testspeech.com'
    env.requirements = 'dev.txt'
    # set_env()


def dev():
    print('Dev')
    env.hosts = [ip]
    env.user = 'django'
    env.password = os.environ['DJANGO_USER_DEV'] #ssh password for user
    env.app_name = 'dev'
    # env.code_dir = 'talkr.pro'
    env.requirements = 'dev.txt'
    # set_env()

def production():
    print('Production')
    env.hosts = [ip]
    env.user = 'django'
    env.password = os.environ['DJANGO_USER_PROD'] #ssh password for user
    env.app_name = 'production'
    env.code_dir = 'domain'
    env.requirements = 'production.txt'
    # set_env()

def start():
    run('celery -A speech worker -l info')
    run('./manage.py runserver 127.0.0.1:8000')

    # with cd('speech/'.format(env.code_dir)):
    #     run('pwd')
    #     with prefix(env.venv):
    #         run('celery -A speech woerker -l info')
    #         run('{} ./manage.py migrate --noinput'.format(env.enviro))
            # run('{} ./manage.py collectstatic --noinput'.format(env.enviro))
            # run('{0} ./manage.py loaddata fixtures/{1}/site.json'.format(env.enviro, env.app_name))
            # run('{} ./manage.py init_payment_plans'.format(env.enviro))


