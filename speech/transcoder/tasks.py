# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import TranscodedAudio



@shared_task
def transcodeTask(instance, transcoder, transformer):
    return (instance, transcoder(instance, transformer).transcode())

@shared_task
def saveTranscode(*args, **kwargs):
    instance = args[0][0]
    transcodedPath = args[0][1]

    ts = TranscodedAudio(speech = instance.speech)
    ts.file.name = transcodedPath
    ts.save()

    instance.delete()

@shared_task
def splitTask(instance, transcoder, transformer):
    return (instance, transcoder(instance, transformer).split())