from rest_framework import serializers
from speech.models import Speech, RawAudio
from transcriber.models import Transcription
from toneAnalyzer.models import Tone



class ToneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tone
        fields = '__all__'


# class DocumentToneSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = DocumentTone
#         fields = '__all__'


class TranscriptionSerializer(serializers.ModelSerializer):
    tones = ToneSerializer(many=True, read_only=True)
    # sentence_tones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sentencetone-detail')
    class Meta:
        model = Transcription
        fields = ('id', 'transcription', 'confidence', 'audio', 'tones')


class RawAudioSerializer(serializers.ModelSerializer):
    transcriptions  = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='transcription-detail')
    class Meta:
        model = RawAudio
        fields = ('id', 'transcriptions', 'audio', 'documentTranscription', )

