from django import forms
from .models import Empleo

class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = ['puesto', 'nivel_laboral', 'carga_horaria', 'salario',
                  'contenido', 'modalidad', 'vacantes', 'categoria', 'localidad', 'empresa']
