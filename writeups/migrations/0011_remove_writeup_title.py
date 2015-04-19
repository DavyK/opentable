# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0010_auto_20150419_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writeup',
            name='title',
        ),
    ]
