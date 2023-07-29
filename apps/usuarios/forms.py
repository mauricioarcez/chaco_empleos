from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, FileInput ,PasswordInput

class RegistrarUsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','username', 'password1', 'password2','genero','localidad','dni','fecha_nacimiento','imagen']
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'apellido': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'password1': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'genero': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'localidad': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'dni': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            }),
            'imagen': FileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 15px; border: 1px solid #8C8C8C; background: #F0F0F0;',
            })
        }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user