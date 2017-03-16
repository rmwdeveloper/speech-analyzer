import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
from channels import Group
from transcoder.utils import SoxTransformer, Transcoder
from transcriber.utils import Transcriber, GoogleTranscriber
from transcriber.models import Transcription
from toneAnalyzer.utils import ToneAnalyzer


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        output_directory = Transcoder(instance, SoxTransformer).transcode()
        instance.transcoded = True
        instance.transcoded_path = output_directory
        instance.save()

@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        response = Transcriber(instance, GoogleTranscriber).transcribe()

        document_text = ''

        for result in response['response'].get('results', []):
            for alternative in result['alternatives']:
                document_text = ' %s %s.' % (document_text, alternative['transcript'])
                transcript_instance = Transcription.objects.create(audio=instance,
                                                                   transcription=alternative['transcript'],
                                                                   confidence=alternative['confidence'])
                Group('main').send(
                    {'text': json.dumps({'transcription': alternative['transcript'], 'type': 'loadTranscription',
                                         'relation': instance.id,
                                         'id': transcript_instance.id, 'confidence': alternative['confidence']})})
        instance.transcribed = True
        instance.documentTranscription = document_text
        instance.save()


@receiver(post_save, sender=Audio)
def analyze(sender, instance, **kwargs):
    if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
        ##todo: delete audio files
        ToneAnalyzer(instance).analyze()



