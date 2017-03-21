from django.conf import settings
from django.db import models

from common.formatChecker import AudioVideoFileField



class Speech(models.Model):
    created = models.DateTimeField(auto_now_add = True)



class RawAudio(models.Model):
    audio = AudioVideoFileField(upload_to = settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d',
                                           blank=True,
                                           null=True)
    speech = models.ForeignKey(Speech)
    split = models.BooleanField(default = False)

class ChunkedAudio(models.Model):
    raw = models.ForeignKey(RawAudio)
    chunk = models.FileField(upload_to=settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d/') ## change to based on.. RawAudio pk


from . import signals ## should be done with appconfig