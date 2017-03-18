import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audio
from channels import Group
from transcoder.utils import SoxTransformer, Transcoder
from transcoder.tasks import transcodeTask, saveTranscode
from transcriber.utils import Transcriber, GoogleTranscriber
from transcriber.models import Transcription
from transcriber.tasks import transcribeTask, saveTranscription
from toneAnalyzer.utils import ToneAnalyzer, WatsonToneAnalyzer
from toneAnalyzer.models import DocumentTone, SentenceTone

@receiver(post_save, sender=Audio)
def transcode(sender, instance, **kwargs):
    if kwargs.get('created', False):
        transcodeTask.apply_async((instance, Transcoder, SoxTransformer), link=saveTranscode.s())


@receiver(post_save, sender=Audio)
def speechToText(sender, instance, **kwargs):
    if not kwargs.get('created', False) and not instance.transcribed:
        print 'about to transcribe..'
        transcribeTask.apply_async((instance, Transcriber, GoogleTranscriber), link=saveTranscription.s())

        # response = Transcriber(instance, GoogleTranscriber).transcribe()
        #
        # document_text = ''
        #
        # for result in response['response'].get('results', []):
        #     for alternative in result['alternatives']:
        #         document_text = ' %s %s.' % (document_text, alternative['transcript'])
        #         transcript_instance = Transcription.objects.create(audio=instance,
        #                                                            transcription=alternative['transcript'],
        #                                                            confidence=alternative['confidence'])
        #         Group('main').send(
        #             {'text': json.dumps({'transcription': alternative['transcript'], 'type': 'loadTranscription',
        #                                  'relation': instance.id,
        #                                  'id': transcript_instance.id, 'confidence': alternative['confidence']})})
        # instance.transcribed = True
        # instance.documentTranscription = document_text
        # instance.save()


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
