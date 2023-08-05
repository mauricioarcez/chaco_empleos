from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Usuario
from .forms import RegistrarUsuarioForm
# Create your views here.

class RegistrarUsuario(CreateView):
    """
    Vista basada en clase para registrar un nuevo usuario.

    Esta vista permite a los usuarios registrarse en el sitio web. Utiliza la clase CreateView
    para mostrar un formulario de registro personalizado definido en el formulario RegistrarUsuarioForm.
    Una vez que el formulario es enviado y válido, el nuevo usuario será creado en la base de datos.
    Si el registro es exitoso, el usuario será redirigido a la página de inicio de sesión.

    Attributes:
        model (Usuario): El modelo Usuario utilizado para crear un nuevo usuario.
        template_name (str): El nombre del template utilizado para renderizar la página de registro.
        form_class (RegistrarUsuarioForm): La clase del formulario utilizado para el registro del usuario.
        success_url (str): La URL a la que se redirige al usuario después de un registro exitoso.

    """
    
    model = Usuario
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy('apps.usuarios:iniciar_sesion')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
