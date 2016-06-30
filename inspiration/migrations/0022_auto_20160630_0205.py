# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import inspiration.models.InspirationBaseModelMixin


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0021_remove_contributor_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsightTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='inspiration.Insight')),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.AddField(
            model_name='insighttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Tag'),
        ),
    ]