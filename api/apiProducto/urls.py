from django.urls import path, include
from .views import productoObtenido, productoBuscado, productoAgregado, productoModificado, productoBorrado

urlpatterns = [
    # Urls de categoria incluidas en producto
    path('categoria/', include('api.apiCategoria.urls')),
    # Urls de producto
    path('producto/', productoObtenido, name='obtener'),
    path('<int:id>', productoBuscado, name='buscar'),
    path('agregado/', productoAgregado, name='agregado'),
    path('editado/<int:id>/', productoModificado, name='editado'),
    path('borrado/<int:id>/', productoBorrado, name='borrado'),
    # Urls de cuentas
    path('usuario/', include('api.apiCuentas.urls')),
    # Utls de carrito
    path('carrito/', include('api.apiCarrito.urls'))


]
