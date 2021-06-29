from django.urls import path
from .views import iniciarSesion, registro, salir, perfil

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('salir/', salir, name="salir"),
    path('iniciar-sesion/',iniciarSesion, name='iniciarSesion'),
    path('perfil/',perfil, name='perfil'),
]