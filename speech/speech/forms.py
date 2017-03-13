from .models import Audio
from django.forms import ModelForm



class BookForm(ModelForm):
    class Meta:
        model = Audio
        