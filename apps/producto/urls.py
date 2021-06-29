from django.urls import path
from . import views

urlpatterns = [
    path('agregar-juego/', views.agregar ,name='agregar'),
    path('principal/', views.principal, name='principal'),
    path('eliminar/<producto_id>', views.eliminar, name='eliminarP'),
    path('modificar-producto/<producto_id>', views.modificar_producto, name="modificar_producto"),
    path('juegos/', views.juegos, name='juegos'),   
]