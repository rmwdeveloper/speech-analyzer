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
    tones = SentenceToneSerializer(many=True, read_only=True)

    class Meta:
        model = Transcription
        fields = ('id', 'transcription', 'confidence', 'audio', 'tones')


class AudioSerializer(serializers.ModelSerializer):
    transcriptions = TranscriptionSerializer(many=True, read_only=True)
    tones = DocumentToneSerializer(many=True, read_only=True)

    class Meta:
        model = Audio
        fields = ('id', 'transcriptions', 'tones', 'audio', 'documentTranscription', )