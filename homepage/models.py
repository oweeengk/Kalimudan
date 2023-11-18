import datetime

from django.db import models
from django.utils import timezone

from django.db import models

class UploadedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')