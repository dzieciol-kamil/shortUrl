from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Urls(models.Model):
    original_url = models.URLField()
    short_url = models.URLField()
    user = models.ForeignKey('UserProfile', on_delete=models.PROTECT)

    def __str__(self):
        return self.oryginal_url