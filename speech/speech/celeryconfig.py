from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings


## Django settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'speech.settings')

import django
django.setup()

app = Celery('speech')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('myapp.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'

CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}