# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-07-22 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140),
        ),
    ]
