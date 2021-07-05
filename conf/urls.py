"""The URL configuration for the project. """

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls'), name='courses'),
    path('api/auth/', include('users.auth_urls'), name='users-auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
