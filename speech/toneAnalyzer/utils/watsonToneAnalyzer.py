from common.globalLogger import GlobalLogger
from watson_developer_cloud import ToneAnalyzerV3
from django.conf import settings

class WatsonToneAnalyzer:
    def __init__(self):
        self.logger = GlobalLogger
        self.tone_analyzer = ToneAnalyzerV3(
        username=settings.IBM_TONE_ANALYZER_USERNAME,
        password=settings.IBM_TONE_ANALYZER_PASSWORD,
        version='2016-02-11')


    def analyze(self, text):
        return self.tone_analyzer.tone(text=text)