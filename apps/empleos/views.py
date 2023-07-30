from typing import Any
from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Empleo,Categorias
from .forms import EmpleoForm
from apps.comentarios.forms import ComentarioForm

# Create your views here.


class AgregarEmpleo(CreateView, LoginRequiredMixin):
    model = Empleo
    fields = ['puesto','nivel_laboral','carga_horaria','salario','contenido','modalidad','vacantes','categoria','localidad','empresa']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)


class ListaEmpleos(ListView):
    model = Empleo
    template_name = 'empleos/lista_empleos.html'
    context_object_name = 'empleos'
    ordering = ['-fecha_publicacion',]

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context

    

class ListaMisEmpleos(LoginRequiredMixin, ListView):
    model = Empleo
    template_name = 'empleos/mis_empleos.html'
    context_object_name = 'empleos'
    ordering = ['-fecha_publicacion',]
    
    def get_queryset(self):
        return Empleo.objects.filter(empresa__administrador=self.request.user)
    
def ListaEmpleosPorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre = categoria)
    empleos = Empleo.objects.filter(categoria = categorias2[0].id).order_by('fecha_publicacion')
    categorias = Categorias.objects.all()
    template_name = 'empleos/lista_empleos.html'
    contexto = {
        'empleos': empleos,
        'categorias': categorias,
    }
    return render(request, template_name, contexto)
    
class DetalleEmpleo(DetailView):
    model = Empleo
    template_name = 'empleos/detalles_empleo.html'
    context_object_name = 'empleo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleo = context['empleo']
        form = ComentarioForm(initial={'empleo': empleo})
        context['form'] = form

        comentarios = empleo.comentario_set.all()
        context['comentarios'] = comentarios
        return context

 
class EditarEmpleo(UpdateView, LoginRequiredMixin):
    model = Empleo
    form_class = EmpleoForm
    template_name = 'empleos/editar_empleos.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')

class EliminarEmpleo(DeleteView, LoginRequiredMixin):
    model = Empleo
    template_name = 'empleos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')
    