# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Transcription

@shared_task
def transcribeTask(instance, transcriber, transformer):
    return transcriber(instance, transformer).transcribe()


@shared_task
def saveTranscription(*args, **kwargs):
    instance = kwargs.get('instance')
    Transcriber = kwargs.get('transcriber')
    transformer = kwargs.get('transformer')
    transcription = kwargs.get('transcription')

    Transcriber(instance, transformer).saveTranscription(Transcription, transcription)


