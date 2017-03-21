from django.db import models
from transcriber.models import Transcription


class Tone(models.Model):
    transcription = models.ForeignKey(Transcription, related_name='tones')
    score = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    toneName = models.CharField(null = True, max_length = 255)
    categoryName = models.CharField(null = True, max_length = 255)
