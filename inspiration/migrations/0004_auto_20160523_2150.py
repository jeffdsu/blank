# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0003_auto_20160523_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediumcontribution',
            old_name='contribution_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='mediumcontribution',
            name='medium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspiration.Medium'),
        ),
    ]
