# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0022_auto_20160630_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='insight',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
