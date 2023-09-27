import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.username
  