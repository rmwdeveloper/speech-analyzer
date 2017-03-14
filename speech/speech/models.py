from django.db import models
from django.conf import settings
from formatChecker import AudioVideoFileField


class Audio(models.Model):
    audio = AudioVideoFileField(upload_to = settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d',
                                           # content_types=['video/*', 'audio/*'],
                                           # max_upload_size=10485760,
                                           blank=True,
                                           null=True)

    transcodedPath = models.CharField(null = True, max_length = 1000)
    transcoded = models.BooleanField(default=False)
    transcribed = models.BooleanField(default=False)
    toneAnalyzed = models.BooleanField(default=False)
    documentTranscription = models.TextField(null=True, blank=True)
    # transcribedSpeech = models.TextField(null=True)
    # transcriptionConfidence = models.DecimalField(max_digits=5, decimal_places=5, null=True)


class Transcription(models.Model):
    audio = models.ForeignKey(Audio, related_name='transcriptions')
    transcription = models.TextField(null = True)
    confidence = models.DecimalField(max_digits=5, decimal_places=5, null=True)

class Tone(models.Model):
    # transcription = models.ForeignKey(Transcription)
    score = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    toneName = models.CharField(null = True, max_length = 255)
    categoryName = models.CharField(null = True, max_length = 255)

    class Meta:
        abstract = True

class DocumentTone(Tone):
    document = models.ForeignKey(Audio, related_name='tones')

class SentenceTone(Tone):
    sentence = models.ForeignKey(Transcription, related_name='tones')

# class Timestamp(models.Model):
#     audio = models.ForeignKey(Audio)
#     word = models.CharField(max_length =1000)
#     timestampBegin = models.FloatField(null=True)
#     timestampEnd = models.FloatField(null=True)

from . import signals ## should be done with appconfig