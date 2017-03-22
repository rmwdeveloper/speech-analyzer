from os import makedirs
from os.path import join, normpath, exists
from django.conf import settings

def createUploadDirsIfNotExist(*paths):
    path = normpath(join(settings.MEDIA_ROOT, *paths))
    if not exists(path):
        makedirs(path)