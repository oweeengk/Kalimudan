from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
  #return HttpResponse("WTF")
  return render(request, "homepage.html")
