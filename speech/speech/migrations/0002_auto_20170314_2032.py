# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttone',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_tones', to='speech.Audio'),
        ),
        migrations.AlterField(
            model_name='sentencetone',
            name='sentence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentence_tones', to='speech.Transcription'),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcriptions', to='speech.Audio'),
        ),
    ]