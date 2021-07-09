from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Total
from .forms import FormularioTotal

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
def carrito3(request):
    juegoObtener = Total.objects.filter(perfil_id = request.user.perfil.id)     
    total = 0
    listaFormulario = []
    formulario_juego = None
    for juego in juegoObtener:
        formulario_juego = FormularioTotal(instance=juego)
        listaFormulario.append(formulario_juego)

    if request.method == 'POST':
        total = totalCarrito(request.user.perfil.id)
    datos = {
        "obtenido" : juegoObtener,
        "total" : total,
        'lista_formulario': listaFormulario
    }
    return render(request, 'carrito/carrito.html', datos)  

# def carrito2(request):
#     juegoObtener = Total.objects.filter(perfil_id = request.user.perfil.id) 
#     info_carrito = []

#     for juego in juegoObtener:
#         juego_encontrado = Total.objects.get(id = juego.id)
#         juegoFormulario = FormularioTotal(request.POST, instance=juego_encontrado)
#         infoTotal = [juego, juegoFormulario]

#         info_carrito.append(infoTotal)    
    

#     lista = [1,2]
#     lista2 = [3,4]
#     lista3 = [lista, lista2]

#     total = 0
#     if request.method == 'POST':
#         total = totalCarrito(request.user.perfil.id)
#     datos = {
#         "obtenido" : juegoObtener,
#         "total" : total,
#         'lista3': lista3
#     }
#     return render(request, 'carrito/carrito2.html', datos)   

@login_required
def carro(request ,  juego_id, cantidad=1, revision_cantidad=False):
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

