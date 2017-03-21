from __future__ import unicode_literals

import os
import unicodedata
import speech_recognition as sr
from django.conf import settings


class WitTranscriber:

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
        transcription = self.service.recognize_wit(audio, key=settings.WIT_SERVER_KEY)
        return transcription


