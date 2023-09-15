from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Genero(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.genero

class Localidad(models.Model):
    localidad = models.CharField(max_length=20)

    def __str__(self):
        return self.localidad

class Usuario(AbstractUser):
    
    nombre = models.CharField(max_length=20, null=False, default=None)
    apellido = models.CharField(max_length=20, null=False, default=None)
    email = models.EmailField(unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE,null=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,null=False, default=None)
    telefono = models.IntegerField(blank=True, unique=True,default=None,null=True)
    dni = models.CharField(unique=True, max_length=10, null=False)
    fecha_nacimiento = models.DateField('fecha_nacimiento', null=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/usuario_default.png')
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

