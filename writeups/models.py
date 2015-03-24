__author__ = 'davidkavanagh'

from django.db import models
from django.contrib.auth.models import User
from characters.models import Character

# Create your models here.

class Writeup(models.Model):

    author = models.ForeignKey(User)

    author_character = models.ForeignKey(Character, default=1)

    title = models.CharField(max_length=100)

    submission_date = models.DateTimeField(auto_now_add=True)

    last_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    post_content = models.TextField(max_length=20000) #TODO: make rich text!!!

    class Meta:
        ordering = ('-submission_date',)

    def __unicode__(self):
        return '{0} on {1}'.format(self.author, self.submission_date)


class Comment(models.Model):

    author = models.ForeignKey(User)

    writeup = models.ForeignKey(Writeup, default=1)

    submission_date = models.DateTimeField(auto_now_add=True, blank=True)

    last_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    comment_content = models.TextField(max_length=200)

    def __unicode__(self):
            return 'comment by {0}'.format(self.author)

#TODO: Session Summary model
