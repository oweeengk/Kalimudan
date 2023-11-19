from django import forms
from .models import UploadedFile, News

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'date', 'content', 'category', 'image']