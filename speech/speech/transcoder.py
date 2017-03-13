import os
import ffmpy
from django.conf import settings

def getSubpath(filename):
    media_root = os.path.normpath(settings.MEDIA_ROOT)
    return filename.replace(media_root, '')

def changeFileExtension(base):
    new_name = os.path.splitext(base)[0]

def getOutputDirectory(filename):
    subpath = getSubpath(filename)

    pass
def transcodeAudio(file):
    inputs = {}
    outputs = {}
    subpath = getSubpath(file.name)
    inputs[file.name] = None

    outputs['C:\\Users\\rob\\speechExp\\speech\\uploads\\transcoded\\2017\\03\\13\\test.wav'] = None
    transcode = ffmpy.FFmpeg(
        inputs=inputs,
        outputs=outputs
    )
    transcode.run()