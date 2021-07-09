# Generated by Django 3.2.3 on 2021-07-07 00:14

import apps.producto.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_producto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apps.producto.models.cambiar_nombre, verbose_name='Imagen referencial'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.SmallIntegerField(null=True, verbose_name='Cantidad'),
        ),
    ]
