from django.shortcuts import render, redirect
from .carro import Carro
from apps.producto.models import Producto


# Create your views here.

def agregar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id= producto_id)
    carro.agregar_p(producto= producto)
    return redirect("principal")

def eliminar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id= producto_id)
    carro.eliminar_p(producto= producto)
    return redirect("principal")

def restar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id= producto_id)
    carro.restar_producto(producto= producto)
    return redirect("principal")    

def limpiar_carro(request):

    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("principal")      

def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + (float (value ["precio"])* value ["cantidad"])
    return {"importe_total_carro":total}