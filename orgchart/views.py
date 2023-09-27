from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def index(request):
  return HttpResponse("You are at the index of organizational chart file!")
# Create your views here.
