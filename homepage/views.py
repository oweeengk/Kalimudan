from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.template import loader
from .forms import FileUploadForm
from .models import UploadedFile
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


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

@login_required
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


def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            try:
                return redirect(reverse('file_list'))
            except NoReverseMatch as e:
                print(f"Error: {e}")
    else:
        form = FileUploadForm()
    return render(request, 'db/file_upload.html', {'form': form})
def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'db/file_list.html', {'files': files})