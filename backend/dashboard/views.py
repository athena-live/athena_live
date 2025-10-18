"""Views for the operations dashboard."""
from django.urls import reverse
from django.views.generic import TemplateView


class DashboardHomeView(TemplateView):
    """Landing page for operations staff with quick links into the system."""

    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        """Inject common navigation links."""
        context = super().get_context_data(**kwargs)
        context['nav_links'] = [
            {'label': 'Admin', 'url': reverse('admin:index'), 'description': 'Manage core data via Django admin'},
            {'label': 'User Login', 'url': reverse('login'), 'description': 'Sign in with standard credentials'},
            {'label': 'User Dashboard', 'url': reverse('users:dashboard'), 'description': 'Post-login landing page'},
            {'label': 'API: Users', 'url': '/api/users/', 'description': 'Entry point for user APIs'},
            {'label': 'API: Scrapers', 'url': reverse('scrapers-create'), 'description': 'Create and store scraper code'},
        ]
        return context
