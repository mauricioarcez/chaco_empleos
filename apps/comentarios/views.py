from django.shortcuts import render, redirect

from .forms import ComentarioForm
from .models import Comentario

# Create your views here.
def AgregarComentario(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'comentarios/crear_comentario.html'
    return render(request, template_name, contexto)
