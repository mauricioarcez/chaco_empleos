from django.shortcuts import render
from apps.empleos.models import Empleo
from django.views.generic import ListView

class inicio(ListView):
    model = Empleo
    template_name = 'inicio.html'
    context_object_name = 'empleos'
    ordering = ['-fecha_publicacion',]
    paginate_by = 5

'''def inicio(request):
    contexto = {}
    empleos = Empleo.objects.filter().order_by('-id')[:4]
    contexto ['empleos'] = empleos
    return render(request,'inicio.html',contexto)'''