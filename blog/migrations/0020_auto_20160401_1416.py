# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20160401_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filepath',
            field=models.ImageField(upload_to=''),
        ),
    ]
