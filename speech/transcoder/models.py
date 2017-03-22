from os.path import join, normpath
from django.conf import settings
from django.db import models
from speech.models import Speech, RawAudio


def chunk_upload_to_abs(instance, filename):
    return normpath(join(settings.BASE_DIR, 'uploads', settings.CHUNK_PREFIX , str(instance.id), filename))


class TranscodedAudio(models.Model):
    file = models.FileField(upload_to = settings.TRANSCODED_PREFIX + '/%Y/%m/%d',
                                           blank=True,
                                           null=True)
    speech = models.ForeignKey(Speech) ## TODO: Convert To Generic Relation
    split = models.BooleanField(default=False)

class ChunkedAudio(models.Model): ## TODO: Move to transcoder
    transcoded = models.ForeignKey(TranscodedAudio, null=True)
    chunk = models.FileField(upload_to=chunk_upload_to_abs) ## change to based on.. RawAudio pk