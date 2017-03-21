from .models import RawAudio
from django.forms import ModelForm


class RawAudioForm(ModelForm):
    class Meta:
        model = RawAudio
        fields = ['audio', 'speech']