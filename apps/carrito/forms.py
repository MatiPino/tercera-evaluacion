from django import forms
from django.forms import widgets
from .models import Total


class FormularioTotal(forms.ModelForm):
    class Meta:
        model = Total
        fields = 'cantidad'
        widgets={
        'cantidad':forms.NumberInput(attrs={
            'min': 1, 'max': 10, 'value': 1
        })
        }    