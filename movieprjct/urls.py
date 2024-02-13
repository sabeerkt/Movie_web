import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from movieprjct.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("movapp.urls")),
]

# Static files (CSS, JavaScript, images)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media files (uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
