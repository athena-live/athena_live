"""WSGI config for athena_live project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'athena_live.settings')

application = get_wsgi_application()
