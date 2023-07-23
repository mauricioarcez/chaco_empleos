from django.db import models
from django.utils import timezone

from apps.usuarios.models import Usuario
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre

class Empresa(models.Model):

    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True, null=True)
    Localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
    
class Empleo(models.Model):
    
    puesto = models.CharField(max_length=40,null=False)
    publicador = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    contenido = models.TextField()
    localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    nivel_laboral = models.CharField(max_length=20)
    carga_horaria = models.IntegerField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    modalidad = models.CharField(max_length=20)
    vacantes = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ('-fecha_publicacion',)
