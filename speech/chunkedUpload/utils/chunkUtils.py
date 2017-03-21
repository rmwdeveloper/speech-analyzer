import os
from chunkedUpload.models import ChunkedUpload
from django.conf import settings
from speech.models import RawAudio, Speech ## todo: move this somewhere. chunkutils should be standalone
from common.globalLogger import GlobalLogger

def concatenateChunks(identifier):
    chunks = ChunkedUpload.objects.filter(resumableIdentifier = identifier).order_by('resumableChunkNumber')
    try:
        location = os.path.join(settings.MEDIA_ROOT, settings.UNTRANSCODED_PREFIX, chunks[0].resumableFilename)
    except IndexError as e:
        print 'ERROR'
        GlobalLogger.error('Tried to get first chunk before concatentation, but it didnt exist.'
                           'identifier is...%s.  %s') % (str(identifier), e)


    for chunk in chunks:
        with open(location, 'w+b') as newFile:
            with open(chunk.file.path, 'rb') as chunkFile:
                    newFile.write(chunkFile.read())
                    chunkFile.close()
                    chunk.delete()
        newFile.close()

    speech = Speech.objects.create()
    rawAudio = RawAudio(speech = speech)
    rawAudio.audio = os.path.normpath(location)
    rawAudio.save()


