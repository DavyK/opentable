# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0012_auto_20150517_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionsummary',
            options={'ordering': ('-date_added',), 'verbose_name': 'Session Summary'},
        ),
        migrations.AlterModelOptions(
            name='writeup',
            options={'ordering': ('-date_added',), 'verbose_name': 'Write Up'},
        ),
    ]
