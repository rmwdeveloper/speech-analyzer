from django.conf import settings
from django.db import models

from common.formatChecker import AudioVideoFileField


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
