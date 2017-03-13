import ffmpy


def transcodeAudio(file):
    inputs = {}
    outputs = {}
    inputs[file.name] = None
    outputs['C:\\Users\\rob\\speechExp\\speech\\uploads\\transcoded\\2017\\03\\13\\test.wav'] = None
    transcode = ffmpy.FFmpeg(
        inputs=inputs,
        outputs=outputs
    )
    transcode.run()