from django.conf.urls import url
from .views import upload, upload_complete

urlpatterns = [
    url(r'^upload/$', upload),
    url(r'^upload_complete/$', upload_complete),
]
