from common.globalLogger import GlobalLogger

class ToneAnalyzer:
    def __init__(self, transcriptions, toneAnalyzer, **kwargs):
        self.tone_analyzer = toneAnalyzer()
        self.logger = GlobalLogger
        self.transcriptions = transcriptions


    def analyze(self, text):
        return self.tone_analyzer.analyze(text)



## TODO : Convert tone analyzer to a class.
# def analyzeTone(self, instance):
#
#     for transcription in self.transcriptions:
#         tone = self.tone_analyzer.analyze(transcription.transcription)
#         for category in tone['document_tone']['tone_categories']:
#             for category_tone in category['tones']:
#                 SentenceTone.objects.create(sentence=transcription, score=category_tone['score'],
#                                     toneName=category_tone['tone_name'], categoryName=category['category_name'],
#                                     )
#                 Group('main').send({'text': json.dumps({'toneName': category_tone['tone_name'],
#                                                         'relation': transcription.id,
#                                                         'categoryName': category['category_name'],
#                                                         'type': 'loadSentenceTone',
#                                                         'score': category_tone['score'] })})
#
#     tone = self.tone_analyzer.analyze(text=instance.documentTranscription)
#     for category in tone['document_tone']['tone_categories']:
#         for category_tone in category['tones']:
#             DocumentTone.objects.create(document=instance, score=category_tone['score'],
#                                         toneName=category_tone['tone_name'], categoryName=category['category_name'],
#                                         )
#
#             Group('main').send({'text': json.dumps({'toneName': category_tone['tone_name'],
#                                                     'relation': instance.id,
#                                                     'categoryName': category['category_name'],
#                                                     'type': 'loadDocumentTone',
#                                                     'score': category_tone['score']})})
#
#
#     Group('main').send({'text': json.dumps({'type':'analysisComplete'})})
