import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
# from channels import Group
from transcoder.utils import SoxTransformer, Transcoder
# from transcriber.utils.transcriber import Transcriber
# from toneAnalyzer.utils.toneAnalyzer import ToneAnalyzer


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        output_directory = Transcoder(instance, SoxTransformer).transcode()
        instance.transcoded = True
        instance.transcoded_path = output_directory
        instance.save()

# @receiver(post_save, sender=Audio)
# def speechToText(sender, instance, **kwargs):
#     if not kwargs.get('created', False) and not instance.transcribed:
#         Transcriber(instance).transcribe()
#
# @receiver(post_save, sender=Audio)
# def analyze(sender, instance, **kwargs):
#     if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
#         ##todo: delete audio files
#         ToneAnalyzer(instance).analyze()
#
#
#
