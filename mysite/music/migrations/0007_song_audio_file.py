# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=b''),
        ),
    ]
