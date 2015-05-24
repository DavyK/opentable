# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20150523_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='hidden',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
