from django.conf.urls import url, include
from rest_framework import routers
from speech.api import viewsets



api_router = routers.DefaultRouter()

api_router.register('audio', viewsets.AudioViewSet)
# api_router.register('transcription', viewsets.TranscriptionViewSet)
# api_router.register('document_tone', viewsets.DocumentToneViewSet)
# api_router.register('sentence_tone', viewsets.SentenceToneViewSet)



urlpatterns = [url('^speech/api/v1/', include(api_router.urls))]
