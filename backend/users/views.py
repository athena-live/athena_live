"""Views for the users app."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import UserLoginForm


class UserLoginView(LoginView):
    """Render the login form and authenticate the user."""

    template_name = 'users/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        """Send authenticated users to their intended destination or dashboard."""
        return self.get_redirect_url() or reverse_lazy('users:dashboard')


class UserLogoutView(LogoutView):
    """Terminate the current session and return the user to the login page."""

    next_page = reverse_lazy('users:login')


class UserDashboardView(LoginRequiredMixin, TemplateView):
    """Simple landing page for authenticated users."""

    template_name = 'users/dashboard.html'
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'
