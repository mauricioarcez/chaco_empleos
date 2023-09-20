from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import inicio,nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('nosotros/',nosotros,name='nosotros'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('empleos/',include('apps.empleos.urls')),
    path('comentarios/', include('apps.comentarios.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Configuracion antigua
'''
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''