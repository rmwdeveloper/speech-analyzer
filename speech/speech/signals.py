import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
from channels import Group
from transcoder.utils import transcodeAudio
from speechToText.utils import callAPI
from toneAnalyzer.utils import toneAnalyzer as analyzeTone


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        transcodeAudio(instance)
        Group('main').send({'text': json.dumps({'type':'transcodeStart'})})

@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        callAPI(instance)

@receiver(post_save, sender=Audio)
def analyze(sender, instance, **kwargs):
    if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
        ##todo: delete audio files
        analyzeTone(instance)



