"""URL routes for the messaging app."""
from django.urls import path

from . import views

app_name = 'messaging'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
