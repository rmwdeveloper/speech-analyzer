import os
from chunkedUpload.models import ChunkedUpload
from django.conf import settings
from speech.models import Audio ## todo: move this somewhere. chunkutils should be standalone


def concatenateChunks(identifier):
    chunks = ChunkedUpload.objects.filter(resumableIdentifier = identifier).order_by('resumableChunkNumber')
    location = os.path.join(settings.MEDIA_ROOT, settings.UNTRANSCODED_PREFIX, chunks[0].resumableFilename)
    for chunk in chunks:
        with open(location, 'w+b') as newFile:
            with open(chunk.file.path, 'rb') as chunkFile:
                newFile.write(chunkFile.read())
            chunkFile.close()
            chunk.delete()


    audio = Audio()
    audio.audio = os.path.normpath(location)
    audio.save()


