from django.urls import path, include
from . import views

app_name = "homepage"
urlpatterns = [
  path("", views.index, name="index"),
  path("about/", views.about, name="about"),
  path("volunteering/", views.volunteering, name="volunteering"),
  path("projects/", views.projects, name="projects"),
  path("tesda/", views.tesda, name="tesda"),
  path("donate/", views.donate, name="donate"),

  path("about/orgchart", views.orgchart, name="orgchart"),
  path("about/visitkfi", views.visitkfi, name="visitkfi"),
  path("about/accreditations", views.accreditations, name="accreditations"),
  path("about/administration", views.administration, name="administration"),
  path("about/manualofoperations", views.manualofoperations, name="manualofoperations"),

  path('stories/create/', views.StoriesCreateView.as_view(), name='stories_create'),
  path('stories/<str:category>/', views.StoriesListView.as_view(), name='stories_list'),
  path('stories/<str:category>/<slug:slug>/', views.stories_detail, name='stories_detail'),
  path('stories/<str:category>/<slug:slug>/update/', views.StoriesUpdateView.as_view(), name='stories_update'),
  path('stories/<str:category>/<slug:slug>/delete/', views.StoriesDeleteView.as_view(), name='stories_delete'),
  path('stories/', views.StoriesListView.as_view(), name='stories_list'),

  path("volunteering/apply", views.volunteeringapply, name="volunteeringapply"),

  path("projects/information", views.projectsinformation, name="projectsinformation"),
  path("projects/partners", views.projectspartners, name="projectspartners"),

  path("tesda/coursesoffered", views.tesdacoursesoffered, name="tesdacoursesoffered"),
  path("tesda/history", views.tesdahistory, name="tesdahistory"),

  path('db/upload', views.file_upload, name='file_upload'),
  path('db/files', views.file_list, name='file_list'),
]