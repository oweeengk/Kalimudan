from django.contrib import admin
from .models import UploadedFile, Stories


# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(Stories)