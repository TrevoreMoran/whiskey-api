# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskies', '0011_auto_20160511_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='Nothing', max_length=255),
            preserve_default=False,
        ),
    ]
