import sox
from common.globalLogger import GlobalLogger

class SoxTransformer:
    def __init__(self):
        self.logger = GlobalLogger

    def convert(self, filename, output_directory):

        tfm = sox.Transformer()

        tfm.convert(samplerate=16000, n_channels=1)

        try:
            tfm.build(filename, output_directory)
        except Exception as e:
            self.logger.error('Something went wrong using SoX Transformer %s' % (e.message,))
