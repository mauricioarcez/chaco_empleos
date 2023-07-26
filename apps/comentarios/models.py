from django.db import models

from apps.empleos.models import Empleo
from apps.usuarios.models import Usuario

# Create your models here.
class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['-fecha']