from django.db import models
from django.contrib.auth.models import User

from campaigns.models import Campaign

# Create your models here.


class Character(models.Model):

    PC = ('PC', 'PC')
    NPC = ('NP', 'NPC')
    ORG = ('OR', 'Organisation')

    type_choices = [
        PC,
        NPC,
        ORG
    ]

    character_type = models.CharField(max_length=2, choices=type_choices, default=PC[0])

    campaign = models.ForeignKey(Campaign)

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

    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)

    last_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    hidden = models.BooleanField(default=False)

    def __unicode__(self):

        return self.name






