from watson_developer_cloud import ToneAnalyzerV3
from django.conf import settings
from speech.models import Transcription, Tone


def analyzeTone(instance):
    # text = ''
    tone_analyzer = ToneAnalyzerV3(
        username=settings.IBM_TONE_ANALYZER_USERNAME,
        password=settings.IBM_TONE_ANALYZER_PASSWORD,
        version='2016-02-11')

    transcriptions = Transcription.objects.filter( audio = instance)

    for transcription in transcriptions:
        tone = tone_analyzer.tone(text=transcription.transcription)
        for category in tone['document_tone']['tone_categories']:
            for category_tone in category['tones']:
                Tone.objects.create(transcription=transcription, score=category_tone['score'],
                                    toneName=category_tone['tone_name'], categoryName=category['category_name'],
                                    )






    pass