from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('core.urls')),
    path('api/v1/content/', include('content.urls')),
    path('api/v1/public/', include('content.public_urls')),
    path('api/v1/bookings/', include('bookings.urls')),
    path('api/v1/cms/', include('content.cms_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
