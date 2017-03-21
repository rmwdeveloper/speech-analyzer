from django.db import models
from speech.models import Speech

class Transcription(models.Model):
    audio = models.ForeignKey(Speech, related_name='transcriptions') #Convert To Generic Relation
    transcription = models.TextField(null = True)
    confidence = models.DecimalField(max_digits=5, decimal_places=5, null=True)

