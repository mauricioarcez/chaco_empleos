from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    
    GENERO_ELECCION = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_ELECCION)
    curriculum = models.FileField(null=True, blank=True, upload_to='usuarios/curriculums')
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=11,blank=True, unique=True)
    dni = models.IntegerField(max_length=8,unique=True)
    edad = models.IntegerField(max_length=2)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios/imagenes', default='img/usuario_default.png')
    
    def __str__(self):
        return f'{self.nombre}#{self.id}'
    

