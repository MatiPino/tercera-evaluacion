from django.urls import path
from .views import iniciar_sesion, perfilObtenido, perfilBuscado, perfilAgregado, perfilModificado, perfilBorrado

urlpatterns = [
    path('', perfilObtenido, name='obtener'),
    path('<int:id>', perfilBuscado, name='buscado'),
    path('agregado/', perfilAgregado, name='agregado'),
    path('editado/<int:id>/', perfilModificado, name='editado'),
    path('borrado/<int:id>/', perfilBorrado, name='borrado'),
    path('iniciar/', iniciar_sesion, name= 'iniciar_sesion')
]