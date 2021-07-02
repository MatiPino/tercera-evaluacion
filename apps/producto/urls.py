from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-juego/', views.agregar, name='agregar'),
    path('principal/', views.principal, name='principal'),
    path('eliminar/<producto_id>', views.eliminar, name='eliminarP'),
    path('modificar-producto/<producto_id>', views.modificar_producto, name="modificar_producto"),
    path('juegos/', views.juegos, name='juegos'),
    path('busqueda/', views.buscarJuegos, name='buscarJuegos'),
]
