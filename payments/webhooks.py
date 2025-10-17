"""Webhook handlers for the payments app."""
from django.http import HttpRequest, HttpResponse


def handle_webhook(request: HttpRequest) -> HttpResponse:
    """Placeholder webhook handler."""
    return HttpResponse('Webhook received')
