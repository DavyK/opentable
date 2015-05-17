# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='character_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='character_updated',
            new_name='last_edited',
        ),
    ]
