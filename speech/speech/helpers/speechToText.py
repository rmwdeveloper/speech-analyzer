import os
from channels import Group
from django.conf import settings
import speech_recognition as sr


def callAPI(instance):
    # recognize speech using IBM Speech to Text
    IBM_USERNAME = settings.IBM_USERNAME  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = settings.IBM_PASSWORD  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    AUDIO_FILE = instance.audio.file.name
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    try:
        text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        instance.transcribedSpeech = text
        instance.save()
        Group('main').send({'text': text})
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))

    return 'Hello'
