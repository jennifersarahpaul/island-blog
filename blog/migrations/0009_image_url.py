# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160331_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.URLField(null=True, unique=True),
        ),
    ]