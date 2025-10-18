from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .ai import generate_scraper_code
from .models import Scraper


@require_http_methods(["GET", "POST"])
def create_scraper(request):
    company = request.GET.get("company") or request.POST.get("company")
    url = request.GET.get("url") or request.POST.get("url")

    if not company or not url:
        return JsonResponse({"error": "company and url are required"}, status=400)

    code = generate_scraper_code(url, company)
    scraper = Scraper.objects.create(company=company, url=url, code=code)
    return JsonResponse({"id": scraper.id, "status": "saved"})
