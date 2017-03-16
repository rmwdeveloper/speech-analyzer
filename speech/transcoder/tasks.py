# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task




@shared_task
def transcodeTask(instance, transcoder, transformer):
    return (instance, transcoder(instance, transformer).transcode())

@shared_task
def saveTranscode(*args, **kwargs):
    args[0][0].transcoded = True
    args[0][0].transcoded_path = args[0][1]
    args[0][0].save()

