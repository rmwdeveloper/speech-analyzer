from django.db import models
from django.conf import settings



class Audio(models.Model):
    audio = models.FileField(upload_to = settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d')
    transcoded = models.BooleanField(default=False)
    transcribed = models.BooleanField(default=False)
    transcribedSpeech = models.TextField(null=True)
    transcriptionConfidence = models.DecimalField(max_digits=5, decimal_places=5, null=True)

class Timestamp(models.Model):
    audio = models.ForeignKey(Audio)
    word = models.CharField(max_length =1000)
    timestampBegin = models.FloatField(null=True)
    timestampEnd = models.FloatField(null=True)

from . import signals ## should be done with appconfig