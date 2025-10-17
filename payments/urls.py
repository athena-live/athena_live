"""URL routes for the payments app."""
from django.urls import path

from . import views

app_name = 'payments'
urlpatterns = [
    path("", views.placeholder, name="placeholder"),
]
