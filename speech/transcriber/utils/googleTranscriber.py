import time
import base64

import googleapiclient.discovery

from django.conf import settings

class GoogleTranscriber:

    def get_speech_service(self):
        return googleapiclient.discovery.build('speech', 'v1beta1', developerKey=settings.GOOGLE_KEY)

    def get_speech_content(self, instance):
        with open(self.audio_file, 'rb') as speech:
            return base64.b64encode(speech.read())

    def transcribe(self, instance):
        service = self.get_speech_service()
        speech_content = self.get_speech_content(instance)
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
        return response

