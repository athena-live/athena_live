"""Forms for the users app."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):
    """Authentication form with lightweight styling hooks for templates."""

    username = UsernameField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': _('Username')}),
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')}),
    )
