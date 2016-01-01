# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0004_auto_20151230_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='certif',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='news',
            name='abstract',
        ),
    ]
