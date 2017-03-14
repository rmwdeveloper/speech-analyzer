from speech.models import Audio, Transcription, DocumentTone, SentenceTone
from rest_framework import serializers








class SentenceToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentenceTone
        fields = '__all__'


class DocumentToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentTone
        fields = '__all__'


class TranscriptionSerializer(serializers.ModelSerializer):
    sentence_tones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sentencetone-detail')
    class Meta:
        model = Transcription
        fields = ('id', 'transcription', 'confidence', 'audio', 'sentence_tones')


class AudioSerializer(serializers.ModelSerializer):
    document_tones  = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='documenttone-detail')
    transcriptions  = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='transcription-detail')
    class Meta:
        model = Audio
        fields = ('id', 'transcriptions', 'document_tones', 'audio', 'documentTranscription', )

