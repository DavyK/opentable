# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='min_activation_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 12, 23, 40, 38, 739803, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
