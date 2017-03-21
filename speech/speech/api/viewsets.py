from rest_framework.viewsets import ModelViewSet
from speech.api.serializers import  TranscriptionSerializer, ToneSerializer
from speech.models import RawAudio, Speech
from transcriber.models import Transcription
from toneAnalyzer.models import Tone



# class AudioViewSet(ModelViewSet):
#
#     model = Audio
#     queryset = Audio.objects.all()
#     serializer_class = AudioSerializer


class TranscriptionViewSet(ModelViewSet):

    model = Transcription
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer


class ToneViewSet(ModelViewSet):

    model = Tone
    queryset = Tone.objects.all()
    serializer_class = ToneSerializer


