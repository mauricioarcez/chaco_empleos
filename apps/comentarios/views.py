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
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'comentarios/crear_comentario.html'
    return render(request, template_name, contexto)

class EliminarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    
    def get_success_url(self):
        empleo_id = self.object.empleo.pk
        return reverse_lazy('apps.empleos:detalle_empleo', kwargs={'pk': empleo_id})

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario






