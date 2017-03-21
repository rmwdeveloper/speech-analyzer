# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChunkedUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, upload_to=b'temporary/%Y/%m/%d/%H/%M%S')),
                ('resumableFilename', models.CharField(max_length=1000, null=True)),
                ('resumableChunkNumber', models.IntegerField(null=True)),
                ('resumableChunkSize', models.IntegerField(null=True)),
                ('resumableCurrentChunkSize', models.IntegerField(null=True)),
                ('resumableIdentifier', models.CharField(max_length=1000, null=True)),
                ('resumableRelativePath', models.CharField(max_length=1000, null=True)),
                ('resumableTotalChunks', models.IntegerField(null=True)),
                ('resumableTotalSize', models.IntegerField(null=True)),
                ('resumableType', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
