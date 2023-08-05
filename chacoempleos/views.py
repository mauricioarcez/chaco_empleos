from django.shortcuts import render

def inicio(request):
    """
    Vista para la página de inicio.

    Esta vista renderiza el template 'inicio.html' al entrar a la página de inicio del sitio.
    Es una vista simple que no requiere ninguna lógica adicional y no toma ningún parámetro.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'inicio.html' y la envía al cliente.

    """
    
    template_name = 'inicio.html'
    return render(request,template_name)

def nosotros(request):
    """
    Vista para la página "Nosotros".

    Esta vista renderiza el template 'nosotros.html' al entrar en la seccion "Quienes somos"
    de la barra de navegacion. La página "Nosotros" es una sección que proporciona información sobre quiénes
    somos y nuestra misión como organización/proyecto.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el template 'nosotros.html' y la envía al cliente.

    """
    
    template_name = 'nosotros.html'
    return render(request,template_name)
