# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0018_auto_20160621_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributiontype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
