"""athena_live URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users.views import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
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

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
