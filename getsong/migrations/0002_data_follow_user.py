# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='follow_user',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
