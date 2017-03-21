from django.db import models



class BaseChunkedUpload(models.Model):
    """
    Base chunked upload model. This model is abstract (doesn't create a table
    in the database).
    Inherit from this model to implement your own.
    """

    file = models.FileField(max_length=255, upload_to='temporary/%Y/%m/%d/%H/%M%S')
    resumableFilename = models.CharField(max_length=1000, null=True)
    resumableChunkNumber = models.IntegerField(null=True)
    resumableChunkSize = models.IntegerField(null=True)
    resumableCurrentChunkSize = models.IntegerField(null=True)
    resumableIdentifier = models.CharField(max_length = 1000, null=True)
    resumableRelativePath = models.CharField(max_length=1000, null=True)
    resumableTotalChunks = models.IntegerField(null=True)
    resumableTotalSize = models.IntegerField(null=True)
    resumableType = models.CharField(max_length=1000, null=True)


    class Meta:
        abstract = True


class ChunkedUpload(BaseChunkedUpload):
    """
    Default chunked upload model.
    To use it, set CHUNKED_UPLOAD_ABSTRACT_MODEL as True in your settings.
    """
    pass

from . import signals ## should be done with appconfig