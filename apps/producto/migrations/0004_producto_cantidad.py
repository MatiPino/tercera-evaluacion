# Generated by Django 3.2.3 on 2021-07-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_delete_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.SmallIntegerField(null=True, verbose_name='Cantidad de juegos'),
        ),
    ]