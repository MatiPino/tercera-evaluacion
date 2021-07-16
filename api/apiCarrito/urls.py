from django.urls import path, include
from .views import carritoObtenido, carritoBuscado, carritoAgregado , carritoBorrado

urlpatterns = [
    path('', carritoObtenido, name='obtener'),
    path('<int:id>', carritoBuscado, name='buscado'),
    path('agregado/', carritoAgregado, name='agregado'),
    path('borrado/<int:id>/', carritoBorrado, name='borrado')
]