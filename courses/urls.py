"""The URL configuration for the courses application. """

from django.urls import re_path
from rest_framework import routers

from .views import ContactUs, CourseViewSet

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    re_path(r'^contact-us/?$', ContactUs.as_view(), name='contact-us'),
]

urlpatterns += router.urls
