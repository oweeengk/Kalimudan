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
  path("about/factsandfigures", views.factsandfigures, name="factsandfigures"),
  path("about/manualofoperations", views.manualofoperations, name="manualofoperations"),

  
  path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
  path('news/<str:category>/', views.NewsListView.as_view(), name='news_list'),
  path('news/<str:category>/<slug:slug>/', views.news_detail, name='news_detail'),
  path('news/<str:category>/<slug:slug>/update/', views.NewsUpdateView.as_view(), name='news_update'),
  path('news/<str:category>/<slug:slug>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
  path('news/', views.NewsListView.as_view(), name='news_list'),

  path("volunteering/apply", views.volunteeringapply, name="volunteeringapply"),
  path("volunteering/notices", views.volunteeringnotices, name="volunteeringnotices"),

  path("projects/information", views.projectsinformation, name="projectsinformation"),
  path("projects/partners", views.projectspartners, name="projectspartners"),

  path("tesda/coursesoffered", views.tesdacoursesoffered, name="tesdacoursesoffered"),
  path("tesda/information", views.tesdainformation, name="tesdainformation"),

  path('db/upload', views.file_upload, name='file_upload'),
  path('db/files', views.file_list, name='file_list'),
]