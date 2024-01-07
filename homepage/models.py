import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.urls import reverse


class UploadedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Stories(models.Model):
    CATEGORY_CHOICES = [
        ('statements', 'Statements'),
        ('notices', 'Notices'),
        ('projects', 'Projects'),
        ('announcements', 'Announcements'),
        ('meetings', 'Meetings'),
        ('assessments', 'Assessments'),
        ('announcements', 'Announcements'),
        ('teambuilding', 'Teambuilding'),
        ('study tour', 'Study Tour'),
        ('educational', 'Educational'),
        ('exit conference', 'Exit Conference'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='stories_images/', blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('homepage:stories_update', kwargs={'category': self.category, 'slug': self.slug})
    
    def __str__(self):
        formatted_string = f"[{self.category}] {self.title}"
        return formatted_string