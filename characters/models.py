from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):

    player = models.ForeignKey(User)

    name = models.CharField(max_length=100)

    race = models.CharField(max_length=100)

    character_class = models.CharField(max_length=100)

    level = models.IntegerField(default=1)

    biography = models.TextField()

    current_xp = models.BigIntegerField()

    deceased = models.BooleanField(default=False)

    num_deaths = models.IntegerField(default=0)

    character_token = models.ImageField(upload_to='tokens')

    character_added = models.DateTimeField(auto_now_add=True, auto_now=False)

    character_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):

        return self.name






