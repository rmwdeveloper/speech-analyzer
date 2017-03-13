import json
from channels import Group
from channels.sessions import channel_session
from channels.handler import AsgiRequest, AsgiHandler

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Test

def my_consumer(message):
    # Decode the request from message format to a Request object
    django_request = AsgiRequest(message)
    # Run view
    django_response = view(django_request)
    # Encode the response into message format
    for chunk in AsgiHandler.encode_response(django_response):
        message.reply_channel.send(chunk)

@channel_session
def ws_connect(message):
    Group('main').add(message.reply_channel)
    message.channel_session['room'] = 'label'
    message.reply_channel.send({'accept': True})



@channel_session
def ws_receive(message):
    # label = message.channel_session['room']
    # data = json.loads(message['text'])
    # message.reply_channel.send({'text': 'Hey There!'})
    # Group('chat-'+label).send({'text': json.dumps(data)})
    Test.objects.create(foo='test')

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('main').discard(message.reply_channel)

@receiver(post_save, sender=Test, dispatch_uid="test")
def test(sender, instance, **kwargs):
    Group('main').send({
        "text": json.dumps({
            "id": 1,
            "content": 'Content! ! ! !'})})
