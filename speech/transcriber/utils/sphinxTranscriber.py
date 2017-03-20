import speech_recognition as sr



class SphinxTranscriber:

    def __init__(self):
        self.service = sr.Recognizer()

    def transcribe(self, speech_content):
        return self.service.recognize_sphinx(speech_content)


