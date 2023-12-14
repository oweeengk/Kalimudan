from django import forms
from .models import UploadedFile, Stories

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'date', 'file']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class StoriesForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ['title', 'date', 'content', 'category', 'image']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

