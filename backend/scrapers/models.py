from django.db import models


class Scraper(models.Model):
    company = models.CharField(max_length=255)
    url = models.URLField()
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_run = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.company} ({self.url})"


class JobPosting(models.Model):
    scraper = models.ForeignKey(Scraper, on_delete=models.CASCADE, related_name="job_postings")
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
