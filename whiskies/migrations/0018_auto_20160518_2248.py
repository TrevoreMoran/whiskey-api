# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskies', '0017_whiskeyfact'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiskey',
            name='detail_img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='whiskey',
            name='list_img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
