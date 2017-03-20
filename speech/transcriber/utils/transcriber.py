
class Transcriber:
    def __init__(self, instance, transcription_service):
        self.instance = instance
        self.audio_file = instance.transcodedPath
        self.transcription_service = transcription_service()

    def transcribe(self):

        return self.transcription_service.transcribe(self.instance)

