# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0004_speech_toneanalyzed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech',
            name='transcribed',
        ),
    ]