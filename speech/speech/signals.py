from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
from channels import Group
from helpers.transcoder import transcodeAudio
from helpers.speechToText import callAPI


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        transcodeAudio(instance)

@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        callAPI(instance)




