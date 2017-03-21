from django.db import models
from speech.models import Audio

class Transcription(models.Model):
    audio = models.ForeignKey(Audio, related_name='transcriptions')
    transcription = models.TextField(null = True)
    confidence = models.DecimalField(max_digits=5, decimal_places=5, null=True)