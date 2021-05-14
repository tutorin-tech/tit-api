"""The URL configuration for the courses application. """

from rest_framework import routers

from .views import CourseViewSet

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)

urlpatterns = router.urls
