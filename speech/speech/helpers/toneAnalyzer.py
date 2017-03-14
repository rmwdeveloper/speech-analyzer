import json
from watson_developer_cloud import ToneAnalyzerV3
from django.conf import settings
from speech.models import Transcription, DocumentTone, SentenceTone
from channels import Group

def analyzeTone(instance):
    tone_analyzer = ToneAnalyzerV3(
        username=settings.IBM_TONE_ANALYZER_USERNAME,
        password=settings.IBM_TONE_ANALYZER_PASSWORD,
        version='2016-02-11')

    transcriptions = Transcription.objects.filter( audio = instance)

    for transcription in transcriptions:
        tone = tone_analyzer.tone(text=transcription.transcription)
        for category in tone['document_tone']['tone_categories']:
            for category_tone in category['tones']:
                SentenceTone.objects.create(sentence=transcription, score=category_tone['score'],
                                    toneName=category_tone['tone_name'], categoryName=category['category_name'],
                                    )
                Group('main').send({'text': json.dumps({'toneName': category_tone['tone_name'],
                                                        'relation': transcription.id,
                                                        'categoryName': category['category_name'],
                                                        'type': 'loadSentenceTone',
                                                        'score': category_tone['score'] })})

    tone = tone_analyzer.tone(text=instance.documentTranscription)
    for category in tone['document_tone']['tone_categories']:
        for category_tone in category['tones']:
            DocumentTone.objects.create(document=instance, score=category_tone['score'],
                                        toneName=category_tone['tone_name'], categoryName=category['category_name'],
                                        )

            Group('main').send({'text': json.dumps({'toneName': category_tone['tone_name'],
                                                    'relation': instance.id,
                                                    'categoryName': category['category_name'],
                                                    'type': 'loadDocumentTone',
                                                    'score': category_tone['score']})})


    Group('main').send({'text': json.dumps({'type':'analysisComplete'})})
