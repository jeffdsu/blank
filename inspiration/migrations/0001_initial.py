# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 00:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import inspiration.models.InspirationBaseModelMixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateField()),
                ('return_date', models.DateField()),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('middle_initial', models.CharField(max_length=1, null=True)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.TextField()),
                ('valid', models.BooleanField(default=False)),
                ('checkout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspiration.Checkout')),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('list_of_insights', models.TextField()),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateField(null=True)),
                ('summary', models.TextField()),
                ('cover', models.CharField(max_length=255)),
                ('contributors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='inspiration.Contributor')),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='MediumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_url', models.CharField(max_length=255)),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WordToIgnore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
            bases=(models.Model, inspiration.models.InspirationBaseModelMixin.InspirationBaseModelMixIn),
        ),
        migrations.AddField(
            model_name='medium',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspiration.MediumType'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='medium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Medium'),
        ),
        migrations.AddField(
            model_name='insight',
            name='medium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Medium'),
        ),
        migrations.AddField(
            model_name='insight',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checkout',
            name='medium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Medium'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
