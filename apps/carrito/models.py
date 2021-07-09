from django.db import models
from apps.producto.models import Producto
from apps.cuentas.models import Perfil

# Create your models here.

class Total(models.Model):
    cantidad = models.SmallIntegerField(
        'Cantidad', blank=False, null=True)
    valor_total = models.SmallIntegerField(
        'Precio total', blank=False, null=False)
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, null=True)
    perfil= models.ForeignKey(
        Perfil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.valor_total                   