from django.db import models
from apps.categoria.models import Categoria

# Create your models here.


class Producto(models.Model):
    nombre_juego = models.CharField(
        'Nombre del juego', max_length=50, blank=False, null=False)
    precio_juego = models.SmallIntegerField(
        'Precio del juego', blank=False, null=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre_juego
