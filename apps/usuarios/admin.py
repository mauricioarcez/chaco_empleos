from django.contrib import admin
from .models import Usuario, Localidad, Genero
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Localidad)
admin.site.register(Genero)