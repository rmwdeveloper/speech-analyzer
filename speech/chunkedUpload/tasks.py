from __future__ import absolute_import, unicode_literals
import os
from celery import shared_task


@shared_task
def cleanupBlobs(to_delete):
    pass
