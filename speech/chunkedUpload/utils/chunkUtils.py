import os
from chunkedUpload.models import ChunkedUpload
from django.conf import settings
from speech.models import Audio ## todo: move this somewhere. chunkutils should be standalone
from common.globalLogger import GlobalLogger

def concatenateChunks(identifier):
    chunks = ChunkedUpload.objects.filter(resumableIdentifier = identifier).order_by('resumableChunkNumber')
    try:
        location = os.path.join(settings.MEDIA_ROOT, settings.UNTRANSCODED_PREFIX, chunks[0].resumableFilename)
    except IndexError as e:
        GlobalLogger.error('Tried to get first chunk before concatentation, but it didnt exist.'
                           'identifier is...%s.  %s') % (identifier, e)


    for chunk in chunks:
        with open(location, 'w+b') as newFile:
            with open(chunk.file.path, 'rb') as chunkFile:
                newFile.write(chunkFile.read())
            chunkFile.close()
            chunk.delete()
        newFile.close()


    audio = Audio()
    audio.audio = os.path.normpath(location)
    audio.save()


