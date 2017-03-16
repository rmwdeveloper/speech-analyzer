# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 20:31
from __future__ import unicode_literals

import chunkedUpload.models
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
                ('uniqueIdentifier', models.CharField(default=chunkedUpload.models.generate_upload_id, editable=False, max_length=32, unique=True)),
                ('file', models.FileField(max_length=255, upload_to=b'raw/%Y/%m/%d')),
                ('filename', models.CharField(max_length=255)),
                ('offset', models.BigIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
