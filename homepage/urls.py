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
  path("about/orgchart", views.orgchart, name="orgchart"),
  path("about/visitkfi", views.visitkfi, name="visitkfi"),
  path("about/accreditations", views.accreditations, name="accreditations"),
  path("about/administration", views.administration, name="administration"),
  path("about/factsandfigures", views.factsandfigures, name="factsandfigures"),
  path("about/vmgs", views.vmgs, name="vmgs"),
]