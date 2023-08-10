from typing import Any
from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Empleo,Categorias, Empresa
from .forms import EmpleoForm
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario

# Create your views here.


class AgregarEmpleo(CreateView, LoginRequiredMixin):
    """
    Vista para agregar un empleo a la base de datos.

    Esta vista utiliza la clase CreateView para facilitar la creación de un nuevo registro
    de empleo en la base de datos. Requiere que el usuario esté autenticado para acceder a ella,
    como indica la clase LoginRequiredMixin.

    Attributes:
        model (Empleo): El modelo Empleo utilizado para crear un nuevo registro de empleo.
        fields (list): Lista de campos del formulario que se mostrarán para agregar un empleo.
        template_name (str): El nombre del template utilizado para renderizar la página de agregar empleo.
        success_url (str): La URL de redirección después de agregar exitosamente un empleo.

    Methods:
        form_valid(form): Asigna al campo "colaborador" del nuevo empleo el usuario autenticado antes de guardarlo en la base de datos.
        get_form(form_class=None): Filtra las opciones del campo "empresa" basadas en el usuario autenticado,
        mostrando solo las empresas asociadas al usuario como administrador.

    """
    
    model = Empleo
    fields = ['puesto','nivel_laboral','carga_horaria','salario','contenido','modalidad','vacantes','categoria','localidad','empresa']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar las opciones del campo "empresa" basadas en el usuario autenticado
        form.fields['empresa'].queryset = Empresa.objects.filter(administrador=self.request.user)
        return form


def lista_empleos(request):
    """
    Vista para mostrar la lista de empleos en un template.

    Esta vista se encarga de obtener los empleos disponibles y ademas filtrarlos según las opciones de búsqueda
    ingresadas por el usuario mediante el formulario. Luego, ordena los empleos según la opción seleccionada
    (por fecha de publicación o por salario). Finalmente, muestra los empleos paginados en una página web,
    mostrando 10 empleos por página.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista, que puede contener parámetros de búsqueda
        y orden especificados por el usuario.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'empleos/lista_empleos.html' con la lista de empleos
        paginada, las categorías disponibles para filtrar y un buscador por titulo.

    """
    
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
        

class ListaMisEmpleos(UserPassesTestMixin, ListView):
    """
    Vista basada en clase para mostrar los empleos que le pertenecen a un usuario colaborador.

    Esta vista requiere que el usuario esté autenticado para acceder a ella, como indica la clase LoginRequiredMixin.
    Se utiliza la clase ListView para mostrar una lista de empleos asociados al usuario autenticado como colaborador.
    Los empleos se obtienen filtrando el modelo Empleo por el campo 'empresa__administrador' que corresponde al usuario autenticado.

    Attributes:
        model (Empleo): El modelo Empleo utilizado para obtener la lista de empleos asociados al usuario colaborador.
        template_name (str): El nombre del template utilizado para renderizar la página de empleos del usuario.
        context_object_name (str): El nombre del objeto de contexto que se utilizará en el template para los empleos.
        ordering (list): La lista de campos de modelo por los que se ordenarán los empleos.

    Methods:
        get_context_data(**kwargs): Agrega las categorías disponibles al contexto de la página.
        get_queryset() -> QuerySet: Obtiene la lista de empleos asociados al usuario colaborador filtrados por el buscador.
    
    """
    
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
    
    def test_func(self):
        # Verifica si el usuario actual es el administrador de alguna empresa
        return self.request.user.empresa_set.filter(administrador=self.request.user).exists()

    def handle_no_permission(self):
        # Maneja la redirección si el usuario no tiene permiso para acceder
        raise Http404("No tienes empleos para mostrar o no tienes permiso para acceder a esta página")

    

def ListaEmpleosPorCategoria(request, categoria):
    """
    Vista para mostrar la lista de empleos filtrados por una categoría.

    Esta vista se encarga de filtrar los empleos por la categoría especificada en la URL y mostrarlos en una lista.
    Los empleos se obtienen filtrando el modelo Empleo por el campo 'categoria' y la categoría correspondiente al nombre
    especificado en la URL.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista.
        categoria (str): El nombre de la categoría por la cual se van a filtrar los empleos.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'empleos/lista_empleos.html' con la lista de empleos filtrados
        por la categoría y las categorías disponibles para filtrar.

    """
    
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
    """
    Vista para mostrar los detalles específicos de un empleo.

    Esta vista se encarga de obtener y mostrar los detalles específicos de un empleo en particular,
    identificado por su clave primaria (pk). Además, permite a los usuarios autenticados agregar comentarios
    sobre el empleo. Los comentarios se guardan en la base de datos asociados al empleo y al usuario que los creó.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista.
        pk (int): La clave primaria del empleo que se mostrará en detalle.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'empleos/detalles_empleo.html'
        con los detalles del empleo, el formulario para agregar comentarios y los comentarios existentes.

    """
    
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

 
class EditarEmpleo(UserPassesTestMixin, UpdateView):
    """
    Vista basada en clase para editar un empleo del usuario.

    Esta vista requiere que el usuario esté autenticado para acceder a ella, como indica la clase LoginRequiredMixin.
    Utiliza la clase UpdateView para proporcionar un formulario predefinido que permite al usuario editar los detalles
    del empleo seleccionado. La vista muestra el formulario con los datos actuales del empleo y permite al usuario
    modificarlos y guardar los cambios.

    Attributes:
        model (Empleo): El modelo Empleo utilizado para obtener el empleo que se va a editar.
        form_class (EmpleoForm): La clase del formulario utilizado para la edición del empleo.
        template_name (str): El nombre del template utilizado para renderizar la página de edición del empleo.
        success_url (str): La URL a la que se redirige al usuario después de guardar los cambios exitosamente.

    """
    
    model = Empleo
    form_class = EmpleoForm
    template_name = 'empleos/editar_empleos.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')
    
    def test_func(self):
        # Verifica si el usuario actual es un colaborador de la empresa asociada al empleo
        empleo = self.get_object()  # Obtiene el objeto Empleo actual
        empresa = empleo.empresa  # Obtiene la empresa asociada al empleo
        return self.request.user.is_authenticated and self.request.user == empresa.administrador

    def handle_no_permission(self):
        # Maneja la redirección si el usuario no tiene permiso para acceder
        raise Http404("No tienes permiso para acceder a esta página")

class EliminarEmpleo(DeleteView, LoginRequiredMixin):
    """
    Vista basada en clase para eliminar un empleo del usuario.

    Esta vista requiere que el usuario esté autenticado para acceder a ella, como indica la clase LoginRequiredMixin.
    Utiliza la clase DeleteView para proporcionar una confirmación al usuario antes de eliminar el empleo seleccionado.
    La vista muestra una página de confirmación para que el usuario confirme que desea eliminar el empleo y, al confirmar,
    se elimina el empleo de la base de datos.

    Attributes:
        model (Empleo): El modelo Empleo utilizado para obtener el empleo que se va a eliminar.
        template_name (str): El nombre del template utilizado para renderizar la página de confirmación de eliminación.
        success_url (str): La URL a la que se redirige al usuario después de eliminar el empleo exitosamente.

    """
    
    model = Empleo
    template_name = 'empleos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.empleos:mis_empleos')
    
def ordenar_empleo_por(request):
    """
    Vista para ordenar la lista de empleos según una opción seleccionada.

    Esta vista permite al usuario ordenar la lista de empleos por fecha de publicación o por salario,
    según la opción seleccionada en el parámetro 'orden' enviado en la URL de la solicitud HTTP. 
    Si no se proporciona una opción válida, se muestra la lista de empleos sin orden específico.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista, que puede contener el parámetro 'orden'
        con la opción de ordenamiento seleccionada por el usuario.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'empleos/lista_empleos.html'
        con la lista de empleos ordenada según la opción seleccionada.

    """
    
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
    
