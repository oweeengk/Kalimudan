from django.urls import path, include
from . import views

app_name = "homepage"
urlpatterns = [
  path("", views.index, name="index"),
  path("about/", views.about, name="about"),
  path("news/", views.news, name="news"),
  path("volunteering/", views.volunteering, name="volunteering"),
  path("projects/", views.projects, name="projects"),
  path("tesda/", views.tesda, name="tesda"),
]