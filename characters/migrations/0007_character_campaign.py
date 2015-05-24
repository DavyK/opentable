# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from campaigns.models import Campaign

class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20150517_0117'),
        ('characters', '0006_auto_20150524_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='campaign',
            field=models.ForeignKey(default=Campaign.objects.get(pk=2).id, to='campaigns.Campaign'),
            preserve_default=False,
        ),
    ]
