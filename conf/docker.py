"""A module that extends and overrides settings.py via environment variables. """

import os

from dotenv import load_dotenv

from conf.settings import *  # pylint: disable=unused-wildcard-import,wildcard-import

load_dotenv()

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')

DEBUG = os.getenv('DEBUG', '').lower() == 'true'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('PG_NAME', 'tit-api'),
        'USER': os.getenv('PG_USER', 'postgres'),
        'PASSWORD': os.getenv('PG_PASSWORD', 'secret'),
        'HOST': os.getenv('PG_HOST', 'localhost'),
        'PORT': os.getenv('PG_PORT', '5432'),
    }
}

SECRET_KEY = os.environ['SECRET_KEY']  # do not run anything if SECRET_KEY is not set
