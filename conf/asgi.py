"""The ASGI config for the project. """

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.docker')

application = get_asgi_application()
