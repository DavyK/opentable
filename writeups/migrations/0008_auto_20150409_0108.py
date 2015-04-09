# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0007_auto_20150409_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionsummary',
            name='session_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
