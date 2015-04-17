# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0008_auto_20150409_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeup',
            name='post_content',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
