from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Total

# Create your views here.

@login_required
def carrito(request):
    juegoObtener = Total.objects.filter(perfil_id = request.user.perfil.id)     
    total = 0
    if request.method == 'POST':
        total = totalCarrito(request.user.perfil.id)
    datos = {
        "obtenido" : juegoObtener,
        "total" : total,
    }
    return render(request, 'carrito/carrito.html', datos)  


@login_required
def carro(request, juego_id, cantidad=1):
    productoJ = None
    try:
        productoJ = Producto.objects.get(id = juego_id)
        Total(cantidad=cantidad,
              valor_total=0,
              producto=productoJ,
              perfil=request.user.perfil).save()
    except:
       pass
    return redirect('principal')          

@login_required
def elminarCarrito(request, juego_id):
    carritoAgregado = None
    try:
        carritoAgregado = Total.objects.get(id = juego_id)
        carritoAgregado.delete()
    except:
        pass
    return redirect('carrito')

#Funciones
def totalCarrito(usuario_id):
    productos = Total.objects.filter(perfil_id = usuario_id)
    total = 0
    for i in productos:
        total = total + (i.producto.precio_juego * i.cantidad)
    return total

def carrito_cantidad(request, id):
    carrito = Total.objects.get(id = id)
    carrito.cantidad = request.POST["cantidad"]
    carrito.save()
    return redirect('carrito')