from django.urls import path, include
from . import views
from .views import file_list, file_upload
from .views import NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView, news_detail



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

  path('news/', NewsListView.as_view(), name='news_list'),
  path('news/<str:category>/', NewsListView.as_view(), name='news_list'),

  path('news/create/', NewsCreateView.as_view(), name='news_create'),
    
  path('news/<str:category>/<slug:slug>/', news_detail, name='news_detail'),
  path('news/<str:category>/<slug:slug>/update/', NewsUpdateView.as_view(), name='news_update'),
  path('news/<str:category>/<slug:slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),

#  path("news/projects", views.newsprojects, name="newsprojects"),
#  path("news/notices", views.newsnotices, name="newsnotices"),
#  path("news/statements", views.newsstatements, name="newsstatements"),
#  path("news/projects/<slug:news_title>/", views.news_detail, {'category': 'projects'}, name="news_detail_projects"),
#  path("news/notices/<slug:news_title>/", views.news_detail, {'category': 'notices'}, name="news_detail_notices"),
#  path("news/statements/<slug:news_title>/", views.news_detail, {'category': 'statements'}, name="news_detail_statements"),

  path("volunteering/apply", views.volunteeringapply, name="volunteeringapply"),
  path("volunteering/notices", views.volunteeringnotices, name="volunteeringnotices"),

  path("projects/information", views.projectsinformation, name="projectsinformation"),
  path("projects/partners", views.projectspartners, name="projectspartners"),

  path("tesda/coursesoffered", views.tesdacoursesoffered, name="tesdacoursesoffered"),
  path("tesda/information", views.tesdainformation, name="tesdainformation"),

  path('db/upload', file_upload, name='file_upload'),
  path('db/files', file_list, name='file_list'),
]