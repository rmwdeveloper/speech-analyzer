import os
import json
import threading
from channels import Group
import base64
import time
from django.conf import settings
# from speech.models import Timestamp
from watson_developer_cloud import SpeechToTextV1
# import speech_recognition as sr
import googleapiclient.discovery
from speech.models import Transcription

#todo refactor all this trash
def get_speech_service():
    return googleapiclient.discovery.build('speech', 'v1beta1', developerKey=settings.GOOGLE_KEY)

def transcribe(instance):
    AUDIO_FILE = instance.transcoded_path
    with open(AUDIO_FILE, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
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
        time.sleep(1)
        # Get the long running operation with response.
        response = service_request.execute()
        # if hasattr(response['metadata'], 'progressPercent'):
        #     print response['metadata']['progressPercent']
        # else:
        #     print response['metadata']
        print 'working'
        if 'done' in response and response['done']:
            break

    # First print the raw json response


    # Now print the actual transcriptions
    for result in response['response'].get('results', []):
        for alternative in result['alternatives']:
            transcript_instance = Transcription.objects.create(audio=instance, transcription = alternative['transcript'],
                                        confidence=alternative['confidence'])
            Group('main').send({'text': json.dumps({'transcription': alternative['transcript'], 'type': 'loadTranscription',
                                                    'audio': instance.id,
                                                    'id': transcript_instance.id, 'confidence': alternative['confidence']})})
    instance.transcribed = True
    instance.save()
    ##todo: save transcription
    # os.remove(instance.audio.file.name)
    # os.remove(instance.transcoded_path)



def callAPI(instance):
    transcribe(instance)

