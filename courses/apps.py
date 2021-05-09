"""A module that defines a configuration for the courses application. """

from django.apps import AppConfig


class CoursesConfig(AppConfig):
    """A class representing the courses application config. """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
