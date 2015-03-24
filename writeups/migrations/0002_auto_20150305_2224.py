# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('writeups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writeup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('post_content', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-submission_date',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='comment',
            name='writeup',
            field=models.ForeignKey(default='1', to='writeups.Writeup'),
            preserve_default=False,
        ),
    ]
