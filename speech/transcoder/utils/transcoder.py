import os
from django.conf import settings
from common.globalLogger import GlobalLogger

class Transcoder:
    def __init__(self, instance, transformer,  **kwargs):
        self.transformer = transformer()
        self.transcoded_prefix = settings.TRANSCODED_PREFIX
        self.file = instance.audio.file ## Refactor ? Making assumptions on how files are accessed.
        self.media_root = os.path.normpath(settings.MEDIA_ROOT)
        self.subpath = self.getSubpath(self.file.name)
        self.instance = instance
        self.output_settings = kwargs.get('output_settings', '-ar 16000 -ac 1 -y')
        self.output_directory = self.getOutputDirectory()
        self.logger = GlobalLogger

    def createDirectory(self, base):

        stripped_base = base.lstrip(os.path.sep)
        new_directory = os.path.join(self.media_root, self.transcoded_prefix, stripped_base)
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        return new_directory

    def getSubpath(self, filename):
        untranscoded_prefix = settings.UNTRANSCODED_PREFIX
        return filename.replace(os.path.join(self.media_root, untranscoded_prefix), '')

    def getOutputDirectory(self):
        base, name = os.path.split(self.subpath)
        transcoded_directory = self.createDirectory(base)
        old_filename, old_file_extension = os.path.splitext(name)
        new_filename = old_filename + '.raw'
        return os.path.join(transcoded_directory, new_filename)

    def transcode(self):
        try:
            self.transformer.convert(self.file.name, self.output_directory)
            return self.output_directory
        except AttributeError as e:
            self.logger.error('Tried to transcode using the WebService but had an AttributeErro. %s' % (e.message,))
        except Exception as e:
            self.logger.error('Tried to Transcode. %s' % (e.message,))

