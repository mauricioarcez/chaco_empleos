from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
# Create your views here.

class RegistrarUsuario(CreateView):
    model = Usuario
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy('apps.usuarios:iniciar_sesion')
