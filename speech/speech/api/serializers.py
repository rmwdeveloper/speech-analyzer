from speech.models import Audio, Transcription, DocumentTone, SentenceTone
from rest_framework import serializers


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = '__all__'

class TranscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transcription
        fields = '__all__'

class DocumentToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentTone
        fields = '__all__'

class SentenceToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentenceTone
        fields = '__all__'