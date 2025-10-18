import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .ai import generate_scraper_code
from .models import Scraper


@require_http_methods(["GET", "POST"])
def create_scraper(request):
    company = request.GET.get("company") or request.POST.get("company")
    url = request.GET.get("url") or request.POST.get("url")

    if request.method == "POST" and (not company or not url):
        if request.content_type and "application/json" in request.content_type:
            try:
                payload = json.loads(request.body.decode() or "{}")
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON body"}, status=400)
            company = company or payload.get("company")
            url = url or payload.get("url")

    if request.method == "GET" and not company and not url:
        return JsonResponse(
            {
                "instructions": "Provide company and url via query parameters (?company=...&url=...) or POST JSON {'company': ..., 'url': ...}.",
                "example": "/api/scrapers/create/?company=Example&url=https://example.com",
            }
        )

    if not company or not url:
        return JsonResponse({"error": "company and url are required"}, status=400)

    code = generate_scraper_code(url, company)
    scraper = Scraper.objects.create(company=company, url=url, code=code)
    return JsonResponse({"id": scraper.id, "status": "saved"})
