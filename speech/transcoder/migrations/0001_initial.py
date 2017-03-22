# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import transcoder.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('speech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChunkedAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk', models.FileField(upload_to=transcoder.models.chunk_upload_to_abs)),
                ('raw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speech.RawAudio')),
            ],
        ),
        migrations.CreateModel(
            name='TranscodedAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=b'transcoded/%Y/%m/%d')),
                ('speech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speech.Speech')),
            ],
        ),
    ]
