import json
from channels import Group
from django.dispatch import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Audio


@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    print 'test'
    pass
    # Group('main').send({
    #     "text": json.dumps({
    #         "id": 1,
    #         "content": 'Content! ! ! !'})})

