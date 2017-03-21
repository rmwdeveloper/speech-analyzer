import speech_recognition as sr
import os


class SphinxTranscriber:

    def __init__(self):
        self.service = sr.Recognizer()

    def saveTranscription(self, instance, model, transcription): ## todo: Resolve similarity between sphinx and wit
        instance.transcribed = True
        instance.documentTranscription = transcription
        instance.save()

    def transcribe(self, instance):
        audio_path = instance.audio.path

        with sr.AudioFile(os.path.abspath('C:\\Users\\rob\\speechExp\\speech\\uploads\\transcoded\\joey.wav')) as source:
            audio = self.service.record(source)
        transcription = self.service.recognize_sphinx(audio)
        return transcription


