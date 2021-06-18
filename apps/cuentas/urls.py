from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from .views import registro
from. forms import IniciarSesion
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('registro', registro, name='registro')
    path('Iniciar-sesion/', LoginView.as_view(
        template_name='cuentas/iniciarSesion.html',
        authentication_form = IniciarSesion
    ))
]