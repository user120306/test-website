# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
