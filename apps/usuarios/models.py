from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    
    GENERO_ELECCION = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=20,null=True)
    apellido = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_ELECCION,null=True)
    curriculum = models.FileField(null=True, blank=True, upload_to='usuarios/curriculums')
    localidad = models.CharField(max_length=50,null=True)
    telefono = models.IntegerField(blank=True, unique=True,null=True)
    dni = models.IntegerField(unique=True, null=True)
    edad = models.IntegerField(null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios/imagenes', default='img/usuario_default.png')
    
    def __str__(self):
        return f'{self.nombre}#{self.id}'
    

