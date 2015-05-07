# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('rule_set', models.CharField(max_length=100, verbose_name=b'System (version)')),
                ('description', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-submission_date',),
            },
            bases=(models.Model,),
        ),
    ]
