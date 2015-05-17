__author__ = 'davidkavanagh'

from django.db import models
from django.contrib.auth.models import User
from characters.models import Character
from django.utils import timezone

# Create your models here.


class Writeup(models.Model):

    author = models.ForeignKey(User)

    author_character = models.ForeignKey(Character, default=1)

    date_added = models.DateTimeField(auto_now_add=True)

    last_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    post_content = models.TextField()

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Write Up'

    def __unicode__(self):
        return ' by {0}'.format(self.author_character)


class Comment(models.Model):

    author = models.ForeignKey(User)

    writeup = models.ForeignKey(Writeup, default=1)

    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    last_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    comment_content = models.TextField(max_length=200)

    def __unicode__(self):
            return 'comment by {0}'.format(self.author)


class SessionSummary(models.Model):

    gm = models.ForeignKey(User)

    number = models.IntegerField()

    location = models.CharField(max_length=500)

    session_characters = models.ManyToManyField(Character)

    xp_awarded = models.IntegerField()

    summary_content = models.TextField()

    important_npcs = models.CharField(max_length=500)

    date_added = models.DateTimeField(default=timezone.now, verbose_name='Session Date (eg. YYYY-DD-MM 00:00:00)')

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Session Summary'

    def __unicode__(self):
        return 'Session {0}'.format(self.number)



