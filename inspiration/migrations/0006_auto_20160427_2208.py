# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0005_insightkeywords_list_of_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InsightKeywords',
            new_name='BookKeywords',
        ),
        migrations.RenameField(
            model_name='bookkeywords',
            old_name='list_of_lessons',
            new_name='list_of_insights',
        ),
    ]
