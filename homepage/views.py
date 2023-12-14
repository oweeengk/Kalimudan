from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.urls.exceptions import NoReverseMatch
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify


from .forms import FileUploadForm, StoriesForm
from .models import UploadedFile, Stories


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


def storiesnotices(request):
  return render(request, "stories/notices.html")

def storiesprojects(request):
  return render(request, "stories/projects.html")

def storiesstatements(request):
  return render(request, "stories/statements.html")


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

@login_required
def file_list(request):
    files = UploadedFile.objects.all().order_by('-date')
    return render(request, 'db/file_list.html', {'files': files})

@login_required
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

class StoriesListView(ListView):
    model = Stories
    template_name = 'stories/stories_list.html'
    context_object_name = 'stories_list'

    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = Stories.objects.all().order_by('-date')

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['statements_exist'] = any(stories.category == 'statements' for stories in context['stories_list'])
        context['notices_exist'] = any(stories.category == 'notices' for stories in context['stories_list'])
        context['projects_exist'] = any(stories.category == 'projects' for stories in context['stories_list'])

        return context


class StoriesCreateView(CreateView):
    model = Stories
    form_class = StoriesForm
    template_name = 'stories/stories_form.html'
    def form_valid(self, form):
        print("Form is valid:", form.is_valid())
        print("Errors:", form.errors)
        form.instance.slug = original_slug = slugify(form.instance.title)
        count = 1

        while Stories.objects.filter(slug=form.instance.slug).exists():
            form.instance.slug = f"{original_slug}-{count}"
            count += 1

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage:stories_list')

class StoriesUpdateView(UpdateView):
    model = Stories
    form_class = StoriesForm
    template_name = 'stories/stories_form.html'
    def form_valid(self, form):
        # Generate a unique slug based on the title
        form.instance.slug = original_slug = slugify(form.instance.title)
        count = 1

        while Stories.objects.filter(slug=form.instance.slug).exclude(pk=self.object.pk).exists():
            form.instance.slug = f"{original_slug}-{count}"
            count += 1

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage:stories_list')


class StoriesDeleteView(DeleteView):
    model = Stories
    success_url = reverse_lazy('homepage:stories_list')
    template_name = 'stories/stories_confirm_delete.html'
    def get_success_url(self):
        return reverse('homepage:stories_list')

def stories_detail(request, category, slug):
    stories = get_object_or_404(Stories, category=category, slug=slug)
    return render(request, 'stories/stories_detail.html', {'stories': stories})
