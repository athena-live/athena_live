"""Views for the notifications app."""
from django.http import HttpRequest, HttpResponse


def placeholder(request: HttpRequest) -> HttpResponse:
    """Simple placeholder view to confirm routing."""
    return HttpResponse('notifications endpoint placeholder')
