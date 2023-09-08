from .base import *

SECRET_KEY = 'django-insecure-i+@+9hfe@0i7n+d4i8i)i(e6!d92wb0g_=9bc17z)^p*v#yn(n'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
