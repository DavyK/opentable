# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '__first__'),
        ('writeups', '0003_auto_20150305_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeup',
            name='author_character',
            field=models.ForeignKey(default=1, to='characters.Character'),
            preserve_default=True,
        ),
    ]
