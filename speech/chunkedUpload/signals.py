
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage

from .models import ChunkedUpload

@receiver(pre_delete, sender=ChunkedUpload) ## todo move to own signals.py
def deleteFile(sender, instance, **kwargs):
    default_storage.delete(instance.file.path)

