# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0002_auto_20150305_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writeup',
            field=models.ForeignKey(default=1, to='writeups.Writeup'),
            preserve_default=True,
        ),
    ]
