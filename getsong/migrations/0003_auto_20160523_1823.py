# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsong', '0002_data_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='user_url',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
