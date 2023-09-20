from ..logging import *
from .base import *
from dotenv import load_dotenv
import os

load_dotenv(Path.joinpath(BASE_DIR, '.env'))

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

#configuracion para pythonanywhere
#ALLOWED_HOSTS = ['mauricioarcez.pythonanywhere.com']
ALLOWED_HOSTS = [ '*' ]

# Database. configurarla en .env
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT'),
    }
}


STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'