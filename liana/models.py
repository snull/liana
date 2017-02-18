from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField(default="")
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.text

class Token(models.Model):
    token = models.CharField(max_length=8)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return "%s's token" % self.user
