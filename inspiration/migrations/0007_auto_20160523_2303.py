# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0006_auto_20160523_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediumcontribution',
            name='medium',
        ),
        migrations.AlterField(
            model_name='medium',
            name='medium_contributors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediums', to='inspiration.MediumContribution'),
        ),
    ]
