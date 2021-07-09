from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito3, name='carrito'),
    # path('carrito2/', views.carrito2, name='carrito2'),
    path('enviar-carrito/<juego_id>', views.carro, name="carro"),
    # path('modificar-carrito/<idCarrito>/<int:cantidad>', views.carrito2, name="modCarrito"),
    path('eliminar-carrito/<juego_id>', views.elminarCarrito, name="elminar_carrito")
    
]