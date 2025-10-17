"""Views for the jobs app."""
from django.http import HttpRequest, HttpResponse


def placeholder(request: HttpRequest) -> HttpResponse:
    """Simple placeholder view to confirm routing."""
    return HttpResponse('jobs endpoint placeholder')
