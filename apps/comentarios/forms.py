from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields=['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'style': 'max-width: 100%',
                'placeholder': 'Escribe tu comentario aquí...',
            }),
        }
