from django.apps import AppConfig


class ScrapersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scrapers"

    def ready(self) -> None:
        # Import late to avoid scheduler setup during migrations before apps loaded.
        from .tasks import start_scheduler

        start_scheduler()
