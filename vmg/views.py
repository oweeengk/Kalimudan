from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
  return HttpResponse("You are at vmg index!")

# Create your views here.
