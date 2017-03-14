import os
import json
import threading
from channels import Group
import base64
import time
from django.conf import settings
from speech.models import Timestamp
from watson_developer_cloud import SpeechToTextV1
# import speech_recognition as sr
import googleapiclient.discovery

def get_speech_service():
    return googleapiclient.discovery.build('speech', 'v1beta1', developerKey=settings.GOOGLE_KEY)

def transcribe(speech_file):
    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'FLAC',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
            }
        })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()

    # [END send_request]

    name = response['name']
    # Construct a GetOperation request.
    service_request = service.operations().get(name=name)

    while True:
        # Give the server a few seconds to process.
        print('Waiting for server processing...')
        time.sleep(1)
        # Get the long running operation with response.
        response = service_request.execute()

        if 'done' in response and response['done']:
            break

    # First print the raw json response
    print(json.dumps(response['response'], indent=2))

    # Now print the actual transcriptions
    for result in response['response'].get('results', []):
        print('Result:')
        for alternative in result['alternatives']:
            print(u'  Alternative: {}'.format(alternative['transcript']))

    print 'Done!'



def callAPI(instance):
    AUDIO_FILE = instance.audio.file.name
    transcribe(AUDIO_FILE)

