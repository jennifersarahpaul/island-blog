# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 01:14
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20160404_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=django_markdown.models.MarkdownField(null=True),
        ),
    ]