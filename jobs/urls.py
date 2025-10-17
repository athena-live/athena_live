"""URL routes for the jobs app."""
from django.urls import path

from . import views

app_name = 'jobs'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
