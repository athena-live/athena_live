"""URL routes for the posts app."""
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
