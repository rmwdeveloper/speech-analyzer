from rest_framework.viewsets import ModelViewSet
from speech.api.serializers import AudioSerializer, TranscriptionSerializer, DocumentToneSerializer, \
    SentenceToneSerializer
from speech.models import Audio
from transcriber.models import Transcription
from toneAnalyzer.models import SentenceTone, DocumentTone



class AudioViewSet(ModelViewSet):

    model = Audio
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer




class TranscriptionViewSet(ModelViewSet):

    model = Transcription
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer


class DocumentToneViewSet(ModelViewSet):

    model = DocumentTone
    queryset = DocumentTone.objects.all()
    serializer_class = DocumentToneSerializer


class SentenceToneViewSet(ModelViewSet):

    model = SentenceTone
    queryset = SentenceTone.objects.all()
    serializer_class = SentenceToneSerializer