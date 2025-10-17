"""ASGI config for athena_live project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'athena_live.settings')

application = get_asgi_application()
