from django.urls import path
from .views import iniciar_sesion

urlpatterns = [
    path('iniciar/', iniciar_sesion, name= 'iniciar_sesion')
]