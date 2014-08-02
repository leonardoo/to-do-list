from django.db import models


# Create your models here.
class Todo(models.Model):

    activity = models.TextField(verbose_name='Texto')

    def __unicode__(self):
        return "{1} - {0}".format(self.activity, self.id)
