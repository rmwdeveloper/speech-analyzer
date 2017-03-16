from chunkedUpload.models import ChunkedUpload



def concatenateChunks(identifier):
    chunks = ChunkedUpload.objects.filter(resumableIdentifier = identifier).order_by('resumableChunkNumber')
    test = 'C:\\Users\\rob\\Desktop\\sunny.mp4'
    for chunk in chunks:
        with open(test, 'w+b') as newFile, open(chunk.file.file.name, 'rb') as chunkFile:
            newFile.write(chunkFile.read())