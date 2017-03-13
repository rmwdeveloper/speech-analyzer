import os
import json
from channels import Group
from django.conf import settings
from speech.models import Timestamp
from watson_developer_cloud import SpeechToTextV1
# import speech_recognition as sr



def callAPI(instance):
    # recognize speech using IBM Speech to Text
    IBM_USERNAME = settings.IBM_USERNAME  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = settings.IBM_PASSWORD  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    AUDIO_FILE = instance.audio.file.name
    speech_to_text = SpeechToTextV1(
        username=IBM_USERNAME,
        password=IBM_PASSWORD,
        x_watson_learning_opt_out=False
    )
    print 'opening file'
    with open(AUDIO_FILE, 'rb') as audio_file:
        print 'calling api'
        response = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True, continuous=True,
            word_confidence=True)
        print 'response recieved'
        data = response['results'][0]['alternatives'][0]
        t0 = 'test'
        instance.transcribedSpeech = data['transcript']
        instance.transcriptionConfidence = data['confidence']
        instance.transcribed = True
        instance.save()

        for timestamp in data['timestamps']:
            Timestamp.objects.create(audio=instance, word = timestamp[0],
                                     timestampBegin = timestamp[1], timestampEnd=timestamp[2])
        # Group('main').send({'text': text})
    # r = sr.Recognizer()
    # with sr.AudioFile(AUDIO_FILE) as source:
    #     audio = r.record(source)  # read the entire audio file
    #
    # try:
    #     text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    #     instance.transcribedSpeech = text
    #     instance.transcribed = True
    #     instance.save()
    #     Group('main').send({'text': text})
    # except sr.UnknownValueError:
    #     print("IBM Speech to Text could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from IBM Speech to Text service; {0}".format(e))

