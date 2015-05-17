# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0011_remove_writeup_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionsummary',
            options={'ordering': ('-date_added',)},
        ),
        migrations.AlterModelOptions(
            name='writeup',
            options={'ordering': ('-date_added',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='submission_date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='sessionsummary',
            old_name='session_date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='writeup',
            old_name='submission_date',
            new_name='date_added',
        ),
    ]
