import os
import ffmpy
import sox
from channels import Group
from django.conf import settings

## TODO : would be better as a class.. lots of duplication here

def getSubpath(filename):
    media_root = os.path.normpath(settings.MEDIA_ROOT)
    untranscoded_prefix = settings.UNTRANSCODED_PREFIX
    return filename.replace(os.path.join(media_root, untranscoded_prefix), '')

def changeFileExtension(base):
    new_name = os.path.splitext(base)[0]

def createDirectory(base):
    media_root = os.path.normpath(settings.MEDIA_ROOT)
    transcoded_prefix = settings.TRANSCODED_PREFIX
    stripped_base = base.lstrip(os.path.sep)
    new_directory = os.path.join(media_root, transcoded_prefix, stripped_base)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    return new_directory

def getOutputDirectory(filename):
    subpath = getSubpath(filename)
    base, name = os.path.split(subpath)
    transcoded_directory = createDirectory(base)
    old_filename, old_file_extension = os.path.splitext(name)
    new_filename = old_filename + '.raw'
    return os.path.join(transcoded_directory, new_filename)

def transcodeAudio(audio_instance):
    file = audio_instance.audio.file

    inputs = {}
    outputs = {}
    output_directory = getOutputDirectory(file.name)
    inputs[file.name] = None
    outputs[output_directory] = '-ar 16000 -ac 1 -y'

    # transcode = ffmpy.FFmpeg(
    #     inputs=inputs,
    #     outputs=outputs
    # )
    tfm = sox.Transformer()
    tfm.convert(samplerate=16000, n_channels=1)

    try:
        tfm.build(file.name, output_directory)
        audio_instance.transcoded = True
        audio_instance.audio.file.name = output_directory
        audio_instance.save()
        # Group('main').send({'text': 'Transcode Complete.'})

    except ffmpy.FFRuntimeError as e:
        pass
        ## TODO: emit error, LOG IT
