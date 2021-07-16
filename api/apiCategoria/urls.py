from django.urls import path
from .views import categoriaObtenida, categoriaBuscada, categoriaAgregada, categoriaBorrada

urlpatterns = [
    path('', categoriaObtenida, name='llamada'),
    path('<int:id>', categoriaBuscada, name='buscada'),
    path('agregada/', categoriaAgregada, name='agregada'),
    path('borrada/<int:id>/', categoriaBorrada, name='borrada')
]
