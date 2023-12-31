from django.db import models
from django.utils import timezone

from apps.usuarios.models import Usuario
# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=20, null=False, default=None)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'categorias'


class Localidad(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre

class Empresa(models.Model):

    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, default=None)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=False, default=None)
    logo = models.ImageField(null=True, blank=True, upload_to='empleos', default='empleos/logo_default.png')

    def __str__(self):
        return self.nombre
    
    
class Empleo(models.Model):
    
    puesto = models.CharField(max_length=40,null=False)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, null=False, default=None)
    contenido = models.TextField()
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=False, default=None)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    nivel_laboral = models.CharField(max_length=20)
    carga_horaria = models.IntegerField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    modalidad = models.CharField(max_length=20)
    vacantes = models.IntegerField()
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.puesto

    class Meta:
        ordering = ('-fecha_publicacion',)
