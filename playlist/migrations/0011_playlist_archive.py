# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0010_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
