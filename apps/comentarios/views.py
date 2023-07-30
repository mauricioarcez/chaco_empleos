from django.shortcuts import render, redirect

from .forms import ComentarioForm
from .models import Comentario

# Create your views here.
def AgregarComentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            return redirect('empleos:detalle_empleo', pk=comentario.empleo.pk)
    else:
        form = ComentarioForm()
        
    contexto = {
        'form': form,
    }
    
    template_name = 'comentarios/crear_comentario.html'
    return render(request, template_name, contexto)
