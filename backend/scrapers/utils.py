import json
import os
import subprocess
import tempfile
from typing import Any, Dict

from django.utils import timezone

from .models import Scraper


def run_scraper(scraper_id: int) -> Dict[str, Any]:
    scraper = Scraper.objects.get(id=scraper_id)
    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
            f.write(scraper.code)
            temp_file = f.name

        result = subprocess.check_output(["python3", temp_file], timeout=60, text=True)
        data = json.loads(result)
        scraper.last_run = timezone.now()
        scraper.save(update_fields=["last_run"])
        return data
    except Exception as exc:
        return {"error": str(exc)}
    finally:
        if temp_file and os.path.exists(temp_file):
            os.unlink(temp_file)
