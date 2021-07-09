from django import forms
from django.forms import widgets
from .models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'imagen',
            'nombre_juego',
            'precio_juego',
            'categoria',
            'cantidad'
        ]
        widgets = {
            'nombre_juego': forms.TextInput(attrs={
                'class': 'nombre_p form-control bg-secondary text-light',
                'placeholder': 'Nombre del juego'
            }),
            'precio_juego': forms.TextInput(attrs={
                'class': 'precio form-control bg-secondary text-light',
                'type': 'number',
                'placeholder': 'Ingresa el precio del juego'
            })
        }
