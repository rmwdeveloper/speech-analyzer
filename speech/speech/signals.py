import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Audio
from channels import Group
from transcoder.utils import SoxTransformer, Transcoder
from transcoder.tasks import transcodeTask, saveTranscode
from transcriber.utils import Transcriber, GoogleTranscriber, SphinxTranscriber, WitTranscriber
from transcriber.models import Transcription
from transcriber.tasks import transcribeTask, saveTranscription
from toneAnalyzer.utils import ToneAnalyzer, WatsonToneAnalyzer
from toneAnalyzer.models import DocumentTone, SentenceTone


# TODO: Google Transcoder needs..

@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        if settings.ASYNC:
            transcodeTask.apply_async((instance, Transcoder, SoxTransformer), link=saveTranscode.s())
        else:
            instance, transcodedPath = transcodeTask(instance, Transcoder, SoxTransformer)
            saveTranscode((instance, transcodedPath))
            # transcodeTask.apply((instance, Transcoder, SoxTransformer), link=saveTranscode.s())


@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        if int(instance.audio.file.size) <= 10485760: ## FileSize less than 10mb
            transformer = GoogleTranscriber
        elif int(instance.audio.file.size) > 10485760 and int(instance.audio.file.size) <= 20485760: ## Between 10 and 20
            transformer = WitTranscriber
        else: ## Greater than 20 mb
            transformer = SphinxTranscriber
        if settings.ASYNC:
            transcribeTask.apply_async((instance, Transcriber, transformer), link=saveTranscription.s())
        else:
            transformer = SphinxTranscriber
            instance, transcription = transcribeTask(instance, Transcriber, transformer)
            saveTranscription(instance=instance, transcriber=Transcriber, transformer=transformer, transcription=transcription)
            # saveTranscription((instance, transcription ))
            # transcribeTask.apply((instance, Transcriber, transformer), link=saveTranscription.s())



@receiver(post_save, sender=Audio)
def analyze(sender, instance, **kwargs):
    if not kwargs.get('created', False) and instance.transcribed  and not instance.toneAnalyzed:
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
            tones =  tone_analyzer.analyze(transcription.transcription)
            for categories in tones['document_tone']['tone_categories']:
                for tone in categories['tones']:
                    SentenceTone.objects.create(sentence=transcription, score=tone['score'],
                                                toneName=tone['tone_name'],
                                                categoryName=categories['category_name'])
