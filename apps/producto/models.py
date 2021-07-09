from django.db import models
from apps.categoria.models import Categoria
from os.path import join

# Create your models here.
def cambiar_nombre(instance, filename):
    extension = filename.split('.')[-1]
    filename = "{}_{}.{}".format(
        instance.nombre_juego,
        instance.cantidad,
        extension
    )
    return join('Juegos',filename)

class Producto(models.Model):
    imagen = models.ImageField(
        'Imagen', upload_to=cambiar_nombre, blank = True, null= True)
    nombre_juego = models.CharField(
        'Nombre del juego', max_length=50, blank=False, null=False)
    precio_juego = models.SmallIntegerField(
        'Precio del juego', blank=False, null=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)
    cantidad = models.SmallIntegerField(
        'Cantidad', blank=False, null=True)    
    def __str__(self):
        return self.nombre_juego