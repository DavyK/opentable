# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('character_class', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
                ('biography', models.TextField()),
                ('current_xp', models.BigIntegerField()),
                ('deceased', models.BooleanField(default=False)),
                ('num_deaths', models.IntegerField(default=0)),
                ('character_token', models.ImageField(upload_to=b'tokens')),
                ('character_added', models.DateTimeField(auto_now_add=True)),
                ('character_updated', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
