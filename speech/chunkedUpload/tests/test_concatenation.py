from django.test import TestCase
from django.core.files import File
from mock import patch, MagicMock

# from speech.forms import AudioForm


class TestTranscoder(TestCase):
    def setUp(self):
        self.file_mock = MagicMock(spec=File, name='FileMock')
        self.file_mock.name = 'test1.wav'
        # self.audio = Audio()
        # self.audio.audio = self.file_mock.name
        # self.audio.save()

    def tearDown(self):
        pass
        # self.audio.delete()

    # def test_signal(self):
    #     self.assertEqual(1, 1)

