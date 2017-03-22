from pydub import AudioSegment
from pydub.utils import make_chunks
from django.conf import settings
from common.createUploadDirs import createUploadDirsIfNotExist

class PydubTransformer:

    def split(self, instance, chunkModel, upload_to, filePath):
        sound = AudioSegment.from_wav(filePath)
        chunks = make_chunks(sound, 10000)
        for i, chunk in enumerate(chunks):
            createUploadDirsIfNotExist(settings.CHUNK_PREFIX, str(instance.id))
            file_path = upload_to(instance, 'chunk%s.raw' % (i,))
            f = chunk.export(file_path, format="wav")
            chunkModelInstance = chunkModel(transcoded=instance)
            chunkModelInstance.chunk.name = f.name
            chunkModelInstance.order = i
            chunkModelInstance.save()

        instance.split = True
        instance.save()
