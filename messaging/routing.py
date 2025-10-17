"""WebSocket routing for the messaging app."""
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/messaging/", consumers.MessagingConsumer.as_asgi()),
]
