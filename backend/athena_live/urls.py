"""athena_live URL Configuration."""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from scrapers.views import create_scraper
from users.views import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
    path('api/', include('dashboard.urls')),
    path('api/users/', include('users.urls')),
    path("api/scrapers/create/", create_scraper, name="scrapers-create"),
    # path('api/posts/', include('posts.urls')),
    # path('api/network/', include('network.urls')),
    # path('api/messaging/', include('messaging.urls')),
    # path('api/notifications/', include('notifications.urls')),
    # path('api/jobs/', include('jobs.urls')),
    # path('api/search/', include('search.urls')),
    # path('api/analytics/', include('analytics.urls')),
    # path('api/payments/', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
