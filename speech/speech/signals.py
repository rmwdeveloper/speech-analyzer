import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
from channels import Group
from transcoder.utils import Transcoder
from transcriber.utils import Transcriber
from toneAnalyzer.utils import ToneAnalyzer


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Transcoder(instance).transcode()

@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        Transcriber(instance).transcribe()

@receiver(post_save, sender=Audio)
def analyze(sender, instance, **kwargs):
    if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
        ##todo: delete audio files
        ToneAnalyzer(instance).analyze()



