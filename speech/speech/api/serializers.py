from rest_framework import serializers
from speech.models import Audio
from transcriber.models import Transcription
from toneAnalyzer.models import SentenceTone, DocumentTone



class SentenceToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentenceTone
        fields = '__all__'


class DocumentToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentTone
        fields = '__all__'


class TranscriptionSerializer(serializers.ModelSerializer):
    sentence_tones = SentenceToneSerializer(many=True, read_only=True)
    # sentence_tones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sentencetone-detail')
    class Meta:
        model = Transcription
        fields = ('id', 'transcription', 'confidence', 'audio', 'sentence_tones')


class AudioSerializer(serializers.ModelSerializer):
    document_tones  = DocumentToneSerializer(many=True, read_only=True)
    transcriptions  = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='transcription-detail')
    class Meta:
        model = Audio
        fields = ('id', 'transcriptions', 'document_tones', 'audio', 'documentTranscription', )

