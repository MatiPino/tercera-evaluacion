from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('enviar-carrito/<juego_id>', views.carro, name="carro"),
    path('eliminar-carrito/<juego_id>', views.elminarCarrito, name="elminar_carrito"),
    path('cantidad/<id>', views.carrito_cantidad, name="carrito_cantidad")
]