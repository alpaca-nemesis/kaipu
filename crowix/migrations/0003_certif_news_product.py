# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0002_auto_20151229_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='certif',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='content ')),
                ('time', models.DateTimeField(verbose_name='time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='content ')),
                ('time', models.DateTimeField(verbose_name='time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='content ')),
                ('tag', models.CharField(max_length=20, verbose_name='tag')),
                ('slug', models.CharField(max_length=256, verbose_name='slug', db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
