"""A module that contains the admin interface of the courses application. """

from django.contrib import admin

from .models import Course, Lesson

admin.site.register(Course)
admin.site.register(Lesson)
