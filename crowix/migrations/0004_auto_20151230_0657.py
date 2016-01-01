# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0003_certif_news_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='abstract',
            field=DjangoUeditor.models.UEditorField(default=datetime.datetime(2015, 12, 30, 6, 57, 42, 72840, tzinfo=utc), verbose_name='abstract '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certif',
            name='abstract',
            field=DjangoUeditor.models.UEditorField(default=datetime.datetime(2015, 12, 30, 6, 57, 48, 982630, tzinfo=utc), verbose_name='abstract '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='abstract',
            field=DjangoUeditor.models.UEditorField(default=datetime.datetime(2015, 12, 30, 6, 57, 54, 409416, tzinfo=utc), verbose_name='abstract '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='abstract',
            field=DjangoUeditor.models.UEditorField(default=datetime.datetime(2015, 12, 30, 6, 57, 59, 697035, tzinfo=utc), verbose_name='abstract '),
            preserve_default=False,
        ),
    ]
