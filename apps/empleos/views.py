from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Empleo

# Create your views here.


class AgregarEmpleo(CreateView):
    model = Empleo
    fields = ['puesto','nivel_laboral','carga_horaria','salario','contenido','modalidad']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('inicio')
