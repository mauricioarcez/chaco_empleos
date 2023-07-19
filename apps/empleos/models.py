from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre


class Empleo(models.Model):
    titulo = models.CharField(max_length=40,null=False)
    contenido = models.TextField()
    localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    nivel_laboral = models.CharField(max_length=20)
    carga_horaria = models.IntegerField()
    fecha_publicacion = models.DateTimeField()
    modalidad = models.CharField(max_length=20)
    vacantes = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ('-fecha_publicacion',)
    
    #id_empresa (agregar)