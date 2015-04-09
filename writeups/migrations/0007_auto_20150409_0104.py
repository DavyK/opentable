# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0006_sessionsummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionsummary',
            name='session_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 1, 4, 4, 248536, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
