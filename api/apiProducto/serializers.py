from apps.producto.models import Producto
from rest_framework import serializers

class ProductoOrganizado(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'imagen',
            'nombre_juego',
            'precio_juego',
            'categoria',
            'cantidad'
            ]