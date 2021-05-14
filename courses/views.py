"""A module that contains the class-based views related to the courses application. """

from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    """Returns both a courses list and a course. """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
