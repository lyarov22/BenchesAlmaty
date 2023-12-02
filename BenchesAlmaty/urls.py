from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mySite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('mySite.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
