# Create your tasks here
from __future__ import absolute_import, unicode_literals
import django
django.setup()
from celery import shared_task
import time
from speech.models import Test


@shared_task
def test():
    time.sleep(3)
    return 'Test test test test'


@shared_task
def myCallback(message):
    Test.objects.create(text=message)