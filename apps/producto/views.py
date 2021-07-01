from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import FormularioProducto
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.


@login_required
def agregar(request):
    formularioP = FormularioProducto()
    if request.method == 'POST':
        formularioP = FormularioProducto(request.POST)
        if formularioP.is_valid():
            formularioP.save()
            return redirect('principal')
    context = {
        'formulario': formularioP,
        'titulo': 'Agregar Juego'
    }
    return render(request, 'agregar/producto.html', context)


@login_required
def principal(request):
    obtenerJ = Producto.objects.all()
    obtenerC = Categoria.objects.all()
    datos = {
        "Juegos": obtenerJ,
        "Categorias": obtenerC
    }
    return render(request, 'principal/principal.html', datos)


def juegos(request):
    obtenerJuego = Producto.objects.all()
    obtenerCategoria = Categoria.objects.all()
    datos = {
        "Juegos": obtenerJuego,
        "Categorias": obtenerCategoria
    }
    return render(request, 'principal/juegos.html', datos)


@login_required
def eliminar(request, producto_id):
    productoAgregado = None
    try:
        productoAgregado = Producto.objects.get(id=producto_id)
        productoAgregado.delete()
    except:
        pass
    return redirect('principal')


@login_required
def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'titulo': 'Editar Producto',
        'formulario': FormularioProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = FormularioProducto(
            data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('principal')
        data["formulario"] = formulario

    return render(request, 'agregar/modificar.html', data)


def generate_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def get_games(gameTitle):
    response = generate_request(
        'https://www.cheapshark.com/api/1.0/games?title=' + gameTitle)
    if response:
        return response

    return ''


def buscarJuegos(request):

    datos = {
        'titulo': 'Búsqueda',
        'juegos': get_games(request.GET['gameTitle'])
    }

    return render(request, 'principal/busquedaJuegos.html', datos)


def inicio(request):

    datos = {
        'titulo': 'Inicio'
    }

    return render(request, 'principal/inicio.html', datos)
