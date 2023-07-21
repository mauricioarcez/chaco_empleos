from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','username', 'password1', 'password2','genero','localidad','dni','fecha_nacimiento','imagen']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user