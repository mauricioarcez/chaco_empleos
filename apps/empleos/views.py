from typing import Any
from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Empleo,Categorias
from .forms import EmpleoForm
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario

# Create your views here.


class AgregarEmpleo(CreateView, LoginRequiredMixin):
    model = Empleo
    fields = ['puesto','nivel_laboral','carga_horaria','salario','contenido','modalidad','vacantes','categoria','localidad','empresa']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)


def lista_empleos(request):
    query = request.GET.get('buscador', '')
    orden = request.GET.get('orden', '')
    categorias = Categorias.objects.all()

    empleos = Empleo.objects.all()

    if query:
        empleos = empleos.filter(puesto__icontains=query)

    if orden == 'fecha':
        empleos = empleos.order_by('fecha_publicacion')
    elif orden == 'salario':
        empleos = empleos.order_by('salario')

    # Dividir la lista de empleos en páginas
    paginator = Paginator(empleos, 10)
    page = request.GET.get('page')
    empleos_paginados = paginator.get_page(page)

    context = {
        'empleos': empleos_paginados,
        'categorias': categorias,
    }
    return render(request, 'empleos/lista_empleos.html', context)
        

class ListaMisEmpleos(LoginRequiredMixin, ListView):
    model = Empleo
    template_name = 'empleos/mis_empleos.html'
    context_object_name = 'empleos'
    ordering = ['-fecha_publicacion',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = Empleo.objects.filter(empresa__administrador=self.request.user)

        if query:
            queryset = queryset.filter(puesto__icontains=query)
        return queryset.order_by('puesto')
    

def ListaEmpleosPorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre = categoria)
    empleos = Empleo.objects.filter(categoria = categorias2[0].id).order_by('-fecha_publicacion')
    categorias = Categorias.objects.all()
    template_name = 'empleos/lista_empleos.html'
    contexto = {
        'empleos': empleos,
        'categorias': categorias,
    }
    return render(request, template_name, contexto)
    
def detalle_empleo(request, pk):
    empleo = Empleo.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(empleo=pk)
    form = ComentarioForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.empleo = empleo
            aux.usuario = request.user
            aux.save()
            form = ComentarioForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'empleo': empleo,
        'form': form,
        'comentarios': comentarios,
    }
    template_name = 'empleos/detalles_empleo.html'
    return render(request, template_name, contexto)

 
class EditarEmpleo(UpdateView, LoginRequiredMixin):
    model = Empleo
    form_class = EmpleoForm
    template_name = 'empleos/editar_empleos.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')

class EliminarEmpleo(DeleteView, LoginRequiredMixin):
    model = Empleo
    template_name = 'empleos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')
    
def ordenar_empleo_por(request):
    orden = request.GET.get('orden', '')
    if orden == 'fecha':
        empleos = Empleo.objects.order_by('fecha_publicacion')
    elif orden == 'salario':
        empleos = Empleo.objects.order_by('salario')
    else:
        empleos = Empleo.objects.all()

    context = {
        'empleos': empleos,
        }
    template_name = 'empleos/lista_empleos.html'
    return render(request, template_name, context)
    