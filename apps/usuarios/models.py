from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuarios/usuario_def.png') #Subir imagen default
    
    def __str__(self):
        return self.username
    

