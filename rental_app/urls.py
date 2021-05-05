from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='main')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('owners/', include('owners.urls', namespace='owners')),
    path('properties/', include('properties.urls', namespace='properties')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
