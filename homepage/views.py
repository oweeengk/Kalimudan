from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from .forms import FileUploadForm, NewsForm
from .models import UploadedFile, News
from django.urls import reverse, reverse_lazy
from django.urls.exceptions import NoReverseMatch
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def index(request):
  return render(request, "homepage.html")

def about(request):
  return render(request, "about.html")

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

def file_list(request):
    files = UploadedFile.objects.all().order_by('-date')
    return render(request, 'db/file_list.html', {'files': files})
def file_upload(request):
    if request.method == 'POST':
        messages.success(request, 'Document uploaded successfully!')
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

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return News.objects.filter(category=category)
        else:
            return News.objects.all()

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'

class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('homepage:news_list')
    template_name = 'news/news_confirm_delete.html'

def news_detail(request, category, slug):
    news = get_object_or_404(News, category=category, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})