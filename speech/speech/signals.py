import json
from channels import Group
from django.dispatch import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Audio
from .transcoder import transcodeAudio

@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        transcodeAudio(instance.audio.file)
        instance.transcoded = True
        instance.save()

    # Group('main').send({
    #     "text": json.dumps({
    #         "id": 1,
    #         "content": 'Content! ! ! !'})})

