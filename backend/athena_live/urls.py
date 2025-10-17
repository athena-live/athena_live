"""athena_live URL Configuration."""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', RedirectView.as_view(pattern_name='admin:index', permanent=True)),
    path('api/admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    # path('api/posts/', include('posts.urls')),
    # path('api/network/', include('network.urls')),
    # path('api/messaging/', include('messaging.urls')),
    # path('api/notifications/', include('notifications.urls')),
    # path('api/jobs/', include('jobs.urls')),
    # path('api/search/', include('search.urls')),
    # path('api/analytics/', include('analytics.urls')),
    # path('api/payments/', include('payments.urls')),
]
