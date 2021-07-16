from apps.carrito.models import Total
from rest_framework import serializers

class CarritoOrganizado(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = [
            'cantidad',
            'valor_total',
            'producto',
            'perfil'
            ]