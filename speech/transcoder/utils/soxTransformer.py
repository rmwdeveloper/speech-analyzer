import sox
from common.globalLogger import GlobalLogger

class SoxTranformer:
    def __init__(self):
        self.logger = GlobalLogger
    def transcode(self):

        tfm = sox.Transformer()

        tfm.convert(samplerate=16000, n_channels=1)

        try:
            tfm.build(self.file.name, self.output_directory)
        except Exception as e:
            self.logger.error('Something went wrong using SoX Transformer %s' % (e.message,))
