from .models import Audio
from django.forms import ModelForm


class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['audio', 'transcoded']