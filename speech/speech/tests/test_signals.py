from django.test import TestCase
from django.core.files import File
from mock import patch, MagicMock
from django.core.files.uploadedfile import SimpleUploadedFile
# from speech.forms import AudioForm

# from speech.forms import AudioForm
from speech.models import Audio


class TestTranscoder(TestCase):
    def setUp(self):
        self.file_mock = SimpleUploadedFile('movie.wav', 'test')
        # self.file_mock = MagicMock(spec=File, name='FileMock')
        # self.file_mock.name = 'test1.wav'
        # self.audio = Audio()
        # self.audio.audio = self.file_mock.name
        # self.audio.save()

    def tearDown(self):
        pass
        # self.audio.delete()

    def test_signal(self):
        with patch('celeryconfig.CELERY_ALWAYS_EAGER', True, create=True):

            self.assertTrue(True)





