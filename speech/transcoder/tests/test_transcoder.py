from django.test import TestCase

from mock import patch, MagicMock
from django.core.files.uploadedfile import SimpleUploadedFile



class TestTranscoder(TestCase):
    def setUp(self):
        pass


    def test_signal(self):
        with patch('speech.celeryconfig.CELERY_ALWAYS_EAGER', True, create=True):

            self.assertTrue(True)