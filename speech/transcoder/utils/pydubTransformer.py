import os
from pydub import AudioSegment
from pydub.utils import make_chunks

class PydubTransformer:

    def split(self, instance, chunkModel):
        sound = AudioSegment.from_wav(instance.audio.path)
        chunks = make_chunks(sound, 10000)
        print 'chunks: %s' % (len(chunks), )

        for i, chunk in enumerate(chunks):
            f = chunk.export("C:\\Users\\rob\speechExp\speech\uploads\\temp2\chunk{0}.wav".format(i), format="wav")
            # rawAudio = chunkModel(raw=instance)
            # rawAudio.chunk = f
            # rawAudio.save()
