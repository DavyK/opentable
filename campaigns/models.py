from django.db import models

# Create your models here.


class Campaign(models.Model):

    name = models.CharField(max_length=50)

    rule_set = models.CharField(max_length=100, verbose_name='System (version)')

    description = models.TextField()

    submission_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-submission_date',)