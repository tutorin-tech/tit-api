"""A module that contains models for the courses application. """

from django.db import models


class Course(models.Model):
    """A class model representing a course. """

    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    """A class model representing a lesson. """

    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    script = models.TextField(default='')
    course = models.ForeignKey(Course, models.CASCADE)

    def __str__(self):
        return f'{self.name}'
