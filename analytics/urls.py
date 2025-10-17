"""URL routes for the analytics app."""
from django.urls import path

from . import views

app_name = 'analytics'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
