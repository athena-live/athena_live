"""athena_live URL Configuration."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
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
