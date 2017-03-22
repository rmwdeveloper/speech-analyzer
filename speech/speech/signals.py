import os
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.files.storage import default_storage

from .models import RawAudio, Speech
from transcoder.models import TranscodedAudio, ChunkedAudio
from transcoder.utils import SoxTransformer, Transcoder, PydubTransformer
from transcoder.tasks import transcodeTask, saveTranscode, splitTask

from transcriber.models import Transcription
from transcriber.utils import Transcriber, GoogleTranscriber, SphinxTranscriber, WitTranscriber
from transcriber.tasks import transcribeTask, saveTranscription

from toneAnalyzer.models import Tone
from toneAnalyzer.utils import ToneAnalyzer, WatsonToneAnalyzer



@receiver(pre_delete, sender=RawAudio) ## todo move to own signals.py
def deleteFile(sender, instance, **kwargs):
    try:
        default_storage.delete(instance.audio.path)
    except WindowsError:
        pass ##todo why is this process locked.


@receiver(post_save, sender=RawAudio) ## Convert to .wav
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        if settings.ASYNC:
            transcodeTask.apply_async((instance, Transcoder, SoxTransformer), link=saveTranscode.s())
        else:
            instance, transcodedPath = transcodeTask(instance, Transcoder, SoxTransformer)
            print 'About to save transcode.. instance, transcodedPath %s %s' % (instance, transcodedPath)
            saveTranscode((instance, transcodedPath))
            # transcodeTask.apply((instance, Transcoder, SoxTransformer), link=saveTranscode.s())

@receiver(post_save, sender=TranscodedAudio)  ## Convert to .wav
def split(sender, instance, **kwargs):
    if not instance.split:
        if settings.ASYNC:
            pass
            # transcodeTask.apply_async((instance, Transcoder, SoxTransformer), link=saveTranscode.s())
        else:
            splitTask(instance, Transcoder, PydubTransformer)

            # instance, transcodedPath = transcodeTask(instance, Transcoder, SoxTransformer)
            # saveTranscode((instance, transcodedPath))
            # transcodeTask.apply((instance, Transcoder, SoxTransformer), link=saveTranscode.s())


@receiver(post_save, sender=TranscodedAudio)
def speechToText(sender, instance, **kwargs):
    if not instance.speech.transcribed and instance.split:
        transformer = GoogleTranscriber
        chunks_to_transcode = ChunkedAudio.objects.filter(transcoded=instance)
        print len(chunks_to_transcode)
        for chunk in chunks_to_transcode:
            if settings.ASYNC:
                transcribeTask.apply_async((chunk, Transcriber, transformer), link=saveTranscription.s())

            else:
                transcription = transcribeTask(chunk, Transcriber, transformer)
                print 'transcription: %s' % (transcription, )
                saveTranscription(instance=chunk, transcriber=Transcriber, transformer=transformer,
                                  transcription=transcription)
        instance.speech.transcribed = True
        instance.speech.save()

@receiver(post_save, sender=Speech)
def analyze(sender, instance, **kwargs):
    if instance.transcribed and not instance.toneAnalyzed:
        ##todo: delete audio files
        transcriptions = Transcription.objects.filter(audio=instance)
        tone_analyzer = ToneAnalyzer(transcriptions, WatsonToneAnalyzer)
        tones = tone_analyzer.analyze(instance.documentTranscription)

        for categories in tones['document_tone']['tone_categories']:
            for tone in categories['tones']:
                DocumentTone.objects.create(document=instance, score=tone['score'],
                                            toneName=tone['tone_name'],
                                            categoryName=categories['category_name'])

        for transcription in transcriptions:
            tones = tone_analyzer.analyze(transcription.transcription)
            for categories in tones['document_tone']['tone_categories']:
                for tone in categories['tones']:
                    SentenceTone.objects.create(sentence=transcription, score=tone['score'],
                                                toneName=tone['tone_name'],
                                                categoryName=categories['category_name'])


        ## below was part of speechToText
        # if int(instance.file.file.size) <= 10485760: ## FileSize less than 10mb
        #     transformer = GoogleTranscriber
        # elif int(instance.file.file.size) > 10485760 and int(instance.audio.file.size) <= 20485760: ## Between 10 and 20
        #     transformer = WitTranscriber
        # else: ## Greater than 20 mb
        #     transformer = SphinxTranscriber
        # if settings.ASYNC:
        #     transcribeTask.apply_async((instance, Transcriber, transformer), link=saveTranscription.s())
        # else:
        #     instance, transcription = transcribeTask(instance, Transcriber, transformer)
        #     saveTranscription(instance=instance, transcriber=Transcriber, transformer=transformer, transcription=transcription)
            # saveTranscription((instance, transcription ))
            # transcribeTask.apply((instance, Transcriber, transformer), link=saveTranscription.s())


#
# @receiver(post_save, sender=Transcription)
# def analyze(sender, instance, **kwargs):
#     if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
#         ##todo: delete audio files
#         transcriptions = Transcription.objects.filter(audio=instance)
#         tone_analyzer = ToneAnalyzer(transcriptions, WatsonToneAnalyzer)
#         tones = tone_analyzer.analyze(instance.documentTranscription)
#
#         for categories in tones['document_tone']['tone_categories']:
#             for tone in categories['tones']:
#                 DocumentTone.objects.create(document=instance, score=tone['score'],
#                                             toneName=tone['tone_name'],
#                                             categoryName=categories['category_name'])
#
#
#         for transcription in transcriptions:
#             tones =  tone_analyzer.analyze(transcription.transcription)
#             for categories in tones['document_tone']['tone_categories']:
#                 for tone in categories['tones']:
#                     SentenceTone.objects.create(sentence=transcription, score=tone['score'],
#                                                 toneName=tone['tone_name'],
#                                                 categoryName=categories['category_name'])
