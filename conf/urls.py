"""The URL configuration for the project. """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls'), name='courses'),
]
