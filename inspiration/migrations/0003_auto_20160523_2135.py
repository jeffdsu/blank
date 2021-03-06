# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import inspiration.models.InspirationBaseModelMixin


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0002_auto_20160523_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContributionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='MediumContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('contribution_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspiration.ContributionType')),
                ('contributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspiration.Contributor')),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.AlterField(
            model_name='medium',
            name='contributors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='inspiration.MediumContribution'),
        ),
    ]
