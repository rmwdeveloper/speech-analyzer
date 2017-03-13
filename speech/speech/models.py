from django.db import models
from django.conf import settings



class Audio(models.Model):
    audio = models.FileField(upload_to = settings.UNTRANSCODED_PREFIX + '/%Y/%m/%d')
    transcoded = models.BooleanField(default=False)
    convertedToAudio = models.BooleanField(default=False)




from . import signals ## should be done with appconfig