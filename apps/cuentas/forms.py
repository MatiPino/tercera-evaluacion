from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets

def agregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form-control'

class RegistroUsuario(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        agregarFormControl(self.visible_fields())

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )