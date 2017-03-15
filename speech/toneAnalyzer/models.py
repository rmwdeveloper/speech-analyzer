from django.db import models
from transcriber.models import Transcription
from speech.models import Audio

class Tone(models.Model):
    # transcription = models.ForeignKey(Transcription)
    score = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    toneName = models.CharField(null = True, max_length = 255)
    categoryName = models.CharField(null = True, max_length = 255)

    class Meta:
        abstract = True

class DocumentTone(Tone):
    document = models.ForeignKey(Audio, related_name='document_tones')

class SentenceTone(Tone):
    sentence = models.ForeignKey(Transcription, related_name='sentence_tones')