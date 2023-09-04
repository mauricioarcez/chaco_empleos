DEBUG = False

ALLOWED_HOSTS = ['mauricioarcez.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'mauricioarcez$default',
        "USER": 'mauricioarcez',
        "PASSWORD": '152318mau',
        "HOST": 'mauricioarcez.mysql.pythonanywhere-services.com',
        "PORT": '3306',
    }
}