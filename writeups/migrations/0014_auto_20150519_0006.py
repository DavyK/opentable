# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0013_auto_20150517_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeup',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
