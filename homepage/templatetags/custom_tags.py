# custom_tags.py

from django import template
from django.urls import reverse  # Import reverse function

register = template.Library()

@register.simple_tag
def is_active(request, url_name):
    if request.path == reverse(url_name):
        return 'active'
    return ''
