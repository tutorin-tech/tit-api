"""A module that contains serializers for the courses application. """

from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializes a lesson. """

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'script', )


class CourseSerializer(serializers.ModelSerializer):
    """Serializes a course. """

    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'lessons', 'preview_image', )


class ContactUsSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Serializes data from Contact Us modal. """

    name = serializers.CharField(required=False)
    email = serializers.EmailField()
    message = serializers.CharField()
    agreement = serializers.BooleanField()
