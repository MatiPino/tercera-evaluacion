from apps.categoria.models import Categoria
from rest_framework import serializers

class CategoriaOrganizada(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']