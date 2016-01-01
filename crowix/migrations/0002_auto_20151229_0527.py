# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artical',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Content',
            new_name='content',
        ),
    ]
