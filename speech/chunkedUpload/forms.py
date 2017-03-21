from .models import ChunkedUpload
from django.forms import ModelForm


class ChunkedUploadForm(ModelForm):
    class Meta:
        model = ChunkedUpload
        fields = ['file', 'resumableFilename', 'resumableChunkNumber', 'resumableChunkSize','resumableCurrentChunkSize',
                  'resumableRelativePath','resumableTotalChunks','resumableTotalSize','resumableType',
                  'resumableIdentifier']