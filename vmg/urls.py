from django.urls import path
from . import views

app_name = "vmg"
urlpatterns = [
  path("vmg/", views.index, name="index"),
]