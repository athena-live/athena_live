"""Signals for the users app."""
from django.dispatch import receiver, Signal

user_placeholder_signal = Signal()


@receiver(user_placeholder_signal)
def handle_user_placeholder(**kwargs) -> None:
    """Placeholder signal handler."""
    _ = kwargs
