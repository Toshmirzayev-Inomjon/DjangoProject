from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yangiliklar/', include('news.urls')),
    path('',include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)