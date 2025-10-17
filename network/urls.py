"""URL routes for the network app."""
from django.urls import path

from . import views

app_name = 'network'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
