from django.conf import settings
from django.db import models

from common.formatChecker import AudioVideoFileField






class Speech(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    # transcribed = models.BooleanField(default=False)
    # toneAnalyzed = models.BooleanField(default=False)
    # documentTranscription = models.TextField(null=True, blank=True)


class RawAudio(models.Model):
    audio = AudioVideoFileField(upload_to = settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d',
                                           blank=True,
                                           null=True)
    speech = models.ForeignKey(Speech)
    # transcoded = models.BooleanField(default=False)



from . import signals ## should be done with appconfig