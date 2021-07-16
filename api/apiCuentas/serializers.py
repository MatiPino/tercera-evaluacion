from apps.cuentas.models import Perfil
from rest_framework import serializers

class PerfilOrganizado(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['usuario']