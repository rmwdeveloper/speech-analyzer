# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Transcription

@shared_task
def transcribeTask(instance, transcriber, transformer):
    return (instance, transcriber(instance, transformer).transcribe())


@shared_task
def saveTranscription(*args, **kwargs):
    instance = args[0][0]
    response = args[0][1]
    document_text = ''
    for result in response['response'].get('results', []):
        for alternative in result['alternatives']:
            document_text = ' %s %s.' % (document_text, alternative['transcript'])
            transcript_instance = Transcription.objects.create(audio=instance,
                                                               transcription=alternative['transcript'],
                                                               confidence=alternative['confidence'])
            # Group('main').send(
            #     {'text': json.dumps({'transcription': alternative['transcript'], 'type': 'loadTranscription',
            #                          'relation': instance.id,
            #                          'id': transcript_instance.id, 'confidence': alternative['confidence']})})
    instance.transcribed = True
    instance.documentTranscription = document_text
    instance.save()

