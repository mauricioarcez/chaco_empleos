from django.contrib import admin
from .models import Empleo, Categorias, Localidad, Empresa


# Register your models here.

admin.site.register(Empleo)
admin.site.register(Categorias)
admin.site.register(Localidad)
admin.site.register(Empresa)
