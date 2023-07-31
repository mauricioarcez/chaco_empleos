from django.shortcuts import render

def inicio(request):
    template_name = 'inicio.html'
    return render(request,template_name)

def nosotros(request):
    template_name = 'nosotros.html'
    return render(request,template_name)