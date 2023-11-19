from django.contrib import admin
from .models import UploadedFile, News


# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(News)