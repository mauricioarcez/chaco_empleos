from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm
from .models import Comentario
from django.urls import reverse_lazy

# Create your views here.


@login_required
def AgregarComentario(request):
    """
    Vista para agregar un comentario.

    Esta vista requiere que el usuario esté autenticado para poder acceder a ella.
    Se utiliza el formulario ComentarioForm para crear un nuevo comentario a partir
    de los datos enviados mediante el método POST. Si el formulario es válido,
    el comentario se guarda en la base de datos.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'comentarios/crear_comentario.html'
        con el formulario ComentarioForm y lo envía al cliente.

    """
    
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'comentarios/crear_comentario.html'
    return render(request, template_name, contexto)

class EliminarComentario(LoginRequiredMixin, DeleteView):
    """
    Vista basada en clase para eliminar un comentario.

    Esta vista requiere que el usuario esté autenticado para poder acceder a ella,
    ya que utiliza la clase LoginRequiredMixin. Permite eliminar un comentario
    asociado a un empleo específico mediante la utilización de la clase DeleteView.

    Attributes:
        model (Comentario): El modelo Comentario utilizado para obtener el comentario a eliminar.

    Methods:
        get_success_url(): Retorna la URL a la que se redirige después de eliminar el comentario
        exitosamente.
        test_func(): Verifica si el usuario autenticado es el mismo que creó el comentario
        que se desea eliminar. Solo el creador del comentario puede eliminarlo.

    """
    
    model = Comentario
    
    def get_success_url(self):
        empleo_id = self.object.empleo.pk
        return reverse_lazy('apps.empleos:detalle_empleo', kwargs={'pk': empleo_id})

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario






