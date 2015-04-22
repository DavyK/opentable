# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '__first__'),
        ('writeups', '0005_auto_20150324_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('location', models.CharField(max_length=500)),
                ('xp_awarded', models.IntegerField()),
                ('summary_content', models.TextField()),
                ('important_npcs', models.CharField(max_length=500)),
                ('session_date', models.DateTimeField(
                    default=datetime.datetime(2015, 4, 9, 1, 3, 57, 145101, tzinfo=utc)
                )),
                ('gm', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('session_characters', models.ManyToManyField(to='characters.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
