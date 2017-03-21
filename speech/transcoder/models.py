from django.conf import settings
from django.db import models
from speech.models import Speech


class TranscodedAudio(models.Model):
    file = models.FileField(upload_to = settings.TRANSCODED_PREFIX + '/%Y/%m/%d',
                                           blank=True,
                                           null=True)
    speech = models.ForeignKey(Speech) ## TODO: Convert To Generic Relation