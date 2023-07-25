from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Empleo

# Create your views here.


class AgregarEmpleo(CreateView, LoginRequiredMixin):
    model = Empleo
    fields = ['puesto','nivel_laboral','carga_horaria','salario','contenido','modalidad','vacantes','categoria','localidad','publicador']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('empleos')
    
    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)


class ListaEmpleos(ListView):
    model = Empleo
    template_name = 'empleos/lista_empleos.html'
    context_object_name = 'empleos'
    ordering = ['-fecha_publicacion',]
    paginate_by = 5
