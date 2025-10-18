from django.core.management.base import BaseCommand

from scrapers.utils import run_scraper


class Command(BaseCommand):
    help = "Run a scraper by ID"

    def add_arguments(self, parser):
        parser.add_argument("scraper_id", type=int)

    def handle(self, *args, **options):
        result = run_scraper(options["scraper_id"])
        self.stdout.write(str(result))
