# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0004_auto_20160523_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspiration.ContributionType'),
        ),
    ]
