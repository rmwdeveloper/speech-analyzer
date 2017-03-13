import os
from django.db import models


def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename)

class Audio(models.Model):
    audio = models.FileField(upload_to = 'raw/%Y/%m/%d')
    transcoded = models.BooleanField(default=False)




from . import signals ## should be done with appconfig