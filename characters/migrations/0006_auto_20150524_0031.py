# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_character_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_type',
            field=models.CharField(default=b'PC', max_length=2, choices=[(b'PC', b'PC'), (b'NP', b'NPC'), (b'OR', b'Organisation')]),
            preserve_default=True,
        ),
    ]
