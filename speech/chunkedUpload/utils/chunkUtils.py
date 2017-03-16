from chunkedUpload.models import ChunkedUpload
from speech.models import Audio

def concatenateChunks(identifier):
    chunks = ChunkedUpload.objects.filter(resumableIdentifier = identifier).order_by('resumableChunkNumber')
    test = 'C:\\Users\\rob\\Desktop\\rendezvous.mov'
    with open(test, 'w+b') as newFile:
        for chunk in chunks:
            print chunk.resumableChunkNumber
            with open(chunk.file.file.name, 'rb') as chunkFile:
                newFile.write(chunkFile.read())

    print 'complete'