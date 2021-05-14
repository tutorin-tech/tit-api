"""A module that contains serializers for the courses application. """

from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializes a lesson. """

    class Meta:
        model = Lesson
        fields = ('name', 'description', )


class CourseSerializer(serializers.ModelSerializer):
    """Serializes a course. """

    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ('name', 'lessons', )
