# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0009_auto_20160524_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediumcontribution',
            name='medium',
        ),
        migrations.RemoveField(
            model_name='medium',
            name='medium_contributors',
        ),
        migrations.AddField(
            model_name='medium',
            name='medium_contributors',
            field=models.ManyToManyField(null=True, to='inspiration.MediumContribution'),
        ),
    ]