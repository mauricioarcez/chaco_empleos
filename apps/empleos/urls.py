from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import AgregarEmpleo, ListaEmpleos, ListaMisEmpleos, ListaEmpleosPorCategoria, detalle_empleo, EditarEmpleo, EliminarEmpleo

app_name = 'apps.empleos'

urlpatterns = [
    path('agregar_empleo/', AgregarEmpleo.as_view(), name='agregar_empleo'),
    path('lista_empleos/', ListaEmpleos.as_view(), name='empleos'),
    path('mis_empleos/', ListaMisEmpleos.as_view(), name='mis_empleos'),
    path('lista_por_categoria/<str:categoria>/',ListaEmpleosPorCategoria,name='lista_por_categoria'),
    path('detalle_empleo/<int:pk>/', detalle_empleo, name='detalle_empleo'),
    path('editar_empleo/<int:pk>/', EditarEmpleo.as_view(), name='editar_empleo' ),
    path('confirmar/<int:pk>/', EliminarEmpleo.as_view(), name='eliminar_empleo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)