import base64

class Transcriber:
    def __init__(self, instance, transcription_service):
        self.instance = instance
        self.audio_file = instance.transcodedPath
        self.transcription_service = transcription_service()

    def transcribe(self):
        with open(self.audio_file, 'rb') as speech:
            speech_content = base64.b64encode(speech.read())

        return self.transcription_service.transcribe(speech_content)

