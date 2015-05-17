from django.db import models
# Create your models here.


class Campaign(models.Model):

    name = models.CharField(max_length=50)

    rule_set = models.CharField(max_length=100, verbose_name='System (version)')

    description = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __unicode__(self):
        return self.name