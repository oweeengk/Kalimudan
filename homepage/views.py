from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
  #return HttpResponse("WTF")
  return render(request, "homepage.html")

def about(request):
  return render(request, "about.html")

def news(request):
  return render(request, "news.html")

def volunteering(request):
  return render(request, "volunteering.html")

def projects(request):
  return render(request, "projects.html")

def tesda(request):
  return render(request, "tesda.html")
