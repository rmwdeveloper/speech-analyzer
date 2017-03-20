# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task




@shared_task
def transcodeTask(instance, transcoder, transformer):
    return (instance, transcoder(instance, transformer).transcode())

@shared_task
def saveTranscode(*args, **kwargs):
    instance = args[0][0]
    transcodedPath = args[0][1]
    instance.transcoded = True
    instance.transcodedPath = transcodedPath
    instance.save()

