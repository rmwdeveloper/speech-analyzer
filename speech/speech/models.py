import os
from django.db import models


def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename)

class Audio(models.Model):
    audio = models.FileField(upload_to = get_upload_path)

class Test(models.Model):
    foo = models.CharField(max_length=255)

