from django import forms
from django.forms import widgets
from .models import Categoria

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre_categoria'
        ]
        widgets = {
            'nombre_categoria': forms.TextInput(attrs={
                'class': 'nombre_c form-control bg-secondary text-light',
                'placeholder': 'Nombre de la Categoria'
            }),
        }