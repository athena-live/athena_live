import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from .ai import generate_scraper_code
from .forms import ScraperCreateForm
from .models import Scraper
from .tasks import schedule_all
from .utils import run_scraper


@require_http_methods(["GET", "POST"])
def create_scraper(request):
    company = request.GET.get("company") or request.POST.get("company")
    url = request.GET.get("url") or request.POST.get("url")
    interval_param = request.GET.get("interval_hours") or request.POST.get("interval_hours")
    active_param = request.GET.get("active") or request.POST.get("active")
    interval_hours = None
    is_active = True

    if request.method == "POST" and (not company or not url):
        if request.content_type and "application/json" in request.content_type:
            try:
                payload = json.loads(request.body.decode() or "{}")
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON body"}, status=400)
            company = company or payload.get("company")
            url = url or payload.get("url")
            interval_param = interval_param or payload.get("interval_hours")
            active_param = active_param or payload.get("active")

    if request.method == "GET" and not company and not url:
        return JsonResponse(
            {
                "instructions": (
                    "Provide company and url via query parameters (?company=...&url=...) "
                    "or POST JSON {'company': ..., 'url': ...}. Optional: interval_hours (>=1, default 24), "
                    "active (true/false)."
                ),
                "example": "/api/scrapers/create/?company=Example&url=https://example.com&interval_hours=12",
            }
        )

    if not company or not url:
        return JsonResponse({"error": "company and url are required"}, status=400)

    if interval_param not in (None, ""):
        try:
            interval_hours = int(interval_param)
            if interval_hours < 1:
                raise ValueError
        except (TypeError, ValueError):
            return JsonResponse({"error": "interval_hours must be a positive integer"}, status=400)
    else:
        interval_hours = 24

    if isinstance(active_param, str):
        is_active = active_param.lower() not in ("0", "false", "off")
    elif isinstance(active_param, bool):
        is_active = active_param
    else:
        is_active = True

    code = generate_scraper_code(url, company)
    scraper = Scraper.objects.create(
        company=company,
        url=url,
        code=code,
        interval_hours=interval_hours,
        active=is_active,
    )
    schedule_all()
    return JsonResponse({"id": scraper.id, "status": "saved"})


class ScraperManagementView(LoginRequiredMixin, TemplateView):
    """UI for operations staff to manage scraper scripts."""

    template_name = "scrapers/manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scrapers'] = Scraper.objects.order_by("-created_at")
        context.setdefault('create_form', ScraperCreateForm())
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action", "create")
        if action == "create":
            form = ScraperCreateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                code = generate_scraper_code(data["url"], data["company"])
                scraper = Scraper.objects.create(
                    company=data["company"],
                    url=data["url"],
                    code=code,
                    interval_hours=data["interval_hours"],
                    active=data["active"],
                )
                schedule_all()
                messages.success(request, f"Scraper '{scraper.company}' created and scheduled every {scraper.interval_hours} hour(s).")
                return redirect("scrapers-manage")

            messages.error(request, "Please correct the errors below.")
            return self.render_to_response(self.get_context_data(create_form=form))

        scraper_id = request.POST.get("scraper_id")
        if not scraper_id:
            messages.error(request, "No scraper selected.")
            return redirect("scrapers-manage")

        try:
            scraper = Scraper.objects.get(id=scraper_id)
        except Scraper.DoesNotExist:
            messages.error(request, "Scraper not found.")
            return redirect("scrapers-manage")

        if action == "toggle":
            scraper.active = not scraper.active
            scraper.save(update_fields=["active"])
            schedule_all()
            state = "activated" if scraper.active else "paused"
            messages.success(request, f"Scraper '{scraper.company}' {state}.")
            return redirect("scrapers-manage")

        if action == "update":
            try:
                interval_hours = int(request.POST.get("interval_hours", scraper.interval_hours))
                if interval_hours < 1:
                    raise ValueError
            except (TypeError, ValueError):
                messages.error(request, "Interval must be a positive integer.")
                return redirect("scrapers-manage")

            scraper.interval_hours = interval_hours
            scraper.save(update_fields=["interval_hours"])
            schedule_all()
            messages.success(request, f"Scraper '{scraper.company}' interval updated to every {interval_hours} hour(s).")
            return redirect("scrapers-manage")

        if action == "run":
            result = run_scraper(scraper.id)
            preview = json.dumps(result, default=str)
            if "error" in result:
                messages.error(request, f"Scraper '{scraper.company}' error: {preview[:500]}")
            else:
                messages.success(request, f"Scraper '{scraper.company}' ran successfully: {preview[:500]}")
            return redirect("scrapers-manage")

        messages.error(request, "Unknown action.")
        return redirect("scrapers-manage")
