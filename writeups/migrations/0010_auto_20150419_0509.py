# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0009_auto_20150417_0311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionsummary',
            options={'ordering': ('-session_date',)},
        ),
        migrations.AlterField(
            model_name='sessionsummary',
            name='session_date',
            field=models.DateTimeField(default=django.utils.timezone.now,
                                       verbose_name=b'Session Date (eg. YYYY-DD-MM 00:00:00)'),
            preserve_default=True,
        ),
    ]
