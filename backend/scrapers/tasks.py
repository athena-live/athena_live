from apscheduler.schedulers.background import BackgroundScheduler
from django.db.utils import OperationalError, ProgrammingError

from .models import Scraper
from .utils import run_scraper

scheduler = BackgroundScheduler()
_scheduler_started = False


def schedule_all() -> None:
    try:
        scheduler.remove_all_jobs()
        for scraper in Scraper.objects.filter(active=True):
            scheduler.add_job(
                run_scraper,
                "interval",
                hours=24,
                args=[scraper.id],
                id=f"scraper-{scraper.id}",
                replace_existing=True,
            )
    except (ProgrammingError, OperationalError):
        # Database tables might not be ready yet (e.g. during migrate).
        return


def start_scheduler() -> None:
    global _scheduler_started

    if _scheduler_started:
        return

    scheduler.start()
    schedule_all()
    _scheduler_started = True
