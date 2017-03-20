import speech_recognition as sr



class SphinxTranscriber:

    def __init__(self):
        self.service = sr.Recognizer()

    def transcribe(self, instance):
        audio_path = instance.audio.path

        with sr.AudioFile(audio_path) as source:
            audio = self.service.record(source)
        transcription = self.service.recognize_sphinx(audio)
        return transcription


