# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0013_auto_20160524_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediumtype',
            name='singular_eng_noun',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='medium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='inspiration.Medium'),
        ),
    ]
