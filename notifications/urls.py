"""URL routes for the notifications app."""
from django.urls import path

from . import views

app_name = 'notifications'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
