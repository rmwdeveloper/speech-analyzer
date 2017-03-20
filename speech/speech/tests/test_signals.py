from django.test import TestCase
from django.core.files import File
from mock import patch, MagicMock
from django.core.files.uploadedfile import SimpleUploadedFile


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
        with patch('speech.signals.transcode') as mocked_signal:
           test =  Audio()
           test.audio = self.file_mock
           test.save()

        # form = AudioForm()
        # form.cleaned_data = {'audio': self.file_mock, 'transcoded': False}
        # form.save()

        # Check that your signal was called.
        # sig(audio, Audio)
        self.assertTrue(mocked_signal.called)

        # Check that your signal was called only once.
        self.assertEqual(mocked_signal.call_count, 1)

        # Do whatever else, like actually checking if your signal logic did well.


