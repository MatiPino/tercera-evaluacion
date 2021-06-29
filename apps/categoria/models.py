from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField('Nombre Categoria', max_length= 50)
    def __str__(self):
        return self.nombre_categoria