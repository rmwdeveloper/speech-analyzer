import json
from channels import Group
import base64
import time
from django.conf import settings
import googleapiclient.discovery
from speech.models import Transcription

#todo refactor all this trash
def get_speech_service():
    return googleapiclient.discovery.build('speech', 'v1beta1', developerKey=settings.GOOGLE_KEY)

def transcribe(instance):
    AUDIO_FILE = instance.transcoded_path
    with open(AUDIO_FILE, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
            }
        })

    response = service_request.execute()



    name = response['name']

    service_request = service.operations().get(name=name)

    while True:

        time.sleep(1)

        response = service_request.execute()

        print 'working'
        if 'done' in response and response['done']:
            break



    document_text = ''

    for result in response['response'].get('results', []):
        for alternative in result['alternatives']:
            document_text =' ' + document_text + ' ' + alternative['transcript'] + '.'
            transcript_instance = Transcription.objects.create(audio=instance, transcription = alternative['transcript'],
                                        confidence=alternative['confidence'])
            Group('main').send({'text': json.dumps({'transcription': alternative['transcript'], 'type': 'loadTranscription',
                                                    'relation': instance.id,
                                                    'id': transcript_instance.id, 'confidence': alternative['confidence']})})
    instance.transcribed = True
    instance.documentTranscription = document_text
    instance.save()


def callAPI(instance):
    transcribe(instance)

