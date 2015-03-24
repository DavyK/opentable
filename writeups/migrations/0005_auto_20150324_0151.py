# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0004_writeup_author_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeup',
            name='post_content',
            field=models.TextField(max_length=20000),
            preserve_default=True,
        ),
    ]
