# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='latitude',
            field=models.FloatField(default=48.4692338),
        ),
        migrations.AddField(
            model_name='article',
            name='longitude',
            field=models.FloatField(default=-123.3698813),
        ),
    ]
