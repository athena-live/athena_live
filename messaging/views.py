"""Views for the messaging app."""
from django.http import HttpRequest, HttpResponse


def placeholder(request: HttpRequest) -> HttpResponse:
    """Simple placeholder view to confirm routing."""
    return HttpResponse('messaging endpoint placeholder')
