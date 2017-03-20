from django.test import TestCase

from mock import patch, MagicMock
from django.core.files.uploadedfile import SimpleUploadedFile



class TestTranscoder(TestCase):
    def setUp(self):
        pass


    def test_signal(self):
        with patch('transcoder.tasks.transcodeTask') as transcodeTask:
                transcodeTask()
                self.assertTrue(transcodeTask.called)