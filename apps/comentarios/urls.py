from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import AgregarComentario, EliminarComentario

app_name = 'apps.comentarios'

urlpatterns = [
    path('crear_comentario/', AgregarComentario.as_view(), name = 'crear_comentario'),
    path('eliminar_comentario/<int:pk>/', EliminarComentario.as_view(), name='eliminar_comentario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
