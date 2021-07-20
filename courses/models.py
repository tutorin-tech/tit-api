"""A module that contains models for the courses application. """

from django.db import models


class Course(models.Model):
    """A class model representing a course. """

    name = models.CharField(max_length=64)
    preview_image = models.ImageField(upload_to='preview_images/', blank=True, null=True)

    def get_sorted_lessons(self):
        """Returns a sorted list of lessons for a current course. """

        sorted_lessons = []

        prev_lesson = self.lesson_set.get(prev=None)
        sorted_lessons.append(prev_lesson)

        for _ in range(self.lesson_set.count() - 1):
            prev_lesson = self.lesson_set.get(prev=prev_lesson)
            sorted_lessons.append(prev_lesson)

        return sorted_lessons

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    """A class model representing a lesson. """

    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    script = models.TextField(default='')
    course = models.ForeignKey(Course, models.CASCADE)
    next = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='prev',
                             blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.name}'
