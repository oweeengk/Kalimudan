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
  path("donate/", views.donate, name="donate"),

  path("about/orgchart", views.orgchart, name="orgchart"),
  path("about/visitkfi", views.visitkfi, name="visitkfi"),
  path("about/accreditations", views.accreditations, name="accreditations"),
  path("about/administration", views.administration, name="administration"),
  path("about/factsandfigures", views.factsandfigures, name="factsandfigures"),
  path("about/manualofoperations", views.manualofoperations, name="manualofoperations"),

  path("news/projects", views.newsprojects, name="newsprojects"),
  path("news/notices", views.newsnotices, name="newsnotices"),
  path("news/statements", views.newsstatements, name="newsstatements"),

  path("volunteering/apply", views.volunteeringapply, name="volunteeringapply"),
  path("volunteering/notices", views.volunteeringnotices, name="volunteeringnotices"),

  path("projects/information", views.projectsinformation, name="projectsinformation"),
  path("projects/partners", views.projectspartners, name="projectspartners"),

  path("tesda/coursesoffered", views.tesdacoursesoffered, name="tesdacoursesoffered"),
  path("tesda/information", views.tesdainformation, name="tesdainformation"),
]