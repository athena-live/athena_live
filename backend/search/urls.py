"""URL routes for the search app."""
from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
