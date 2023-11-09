from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
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

def donate(request):
  return render(request, "donate.html")


def orgchart(request):
  return render(request, "about/orgchart.html")

def visitkfi(request):
  return render(request, "about/visitkfi.html")

def accreditations(request):
  return render(request, "about/accreditations.html")

def administration(request):
  return render(request, "about/administration.html")

def factsandfigures(request):
  return render(request, "about/factsandfigures.html")

def manualofoperations(request):
  return render(request, "about/manualofoperations.html")


def newsnotices(request):
  return render(request, "news/notices.html")

def newsprojects(request):
  return render(request, "news/projects.html")

def newsstatements(request):
  return render(request, "news/statements.html")


def volunteeringapply(request):
  return render(request, "volunteering/apply.html")

def volunteeringnotices(request):
  return render(request, "volunteering/notices.html")


def projectsinformation(request):
  return render(request, "projects/information.html")

def projectspartners(request):
  return render(request, "projects/partners.html")


def tesdacoursesoffered(request):
  return render(request, "tesda/coursesoffered.html")

def tesdainformation(request):
  return render(request, "tesda/information.html")
