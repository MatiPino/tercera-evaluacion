from django.http import request
from django.shortcuts import render, redirect
from .forms import IniciarSesion, RegistroUsuario
from django.contrib.auth import login, logout, authenticate
from .models import Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.
def registro(request):
    formulario = None
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            usuario.save()
            return redirect('iniciarSesion')
    if request.method == 'GET':
        formulario = RegistroUsuario()
    contexto = {
        'formulario': formulario
    }            
    return render(request, 'registrar/registro.html', context= contexto)
@login_required
def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('iniciarSesion')  

def iniciarSesion(request):
    formulario = None
    if request.method == "GET":
        formulario = IniciarSesion(request)
    if request.method == "POST":
        usuario = request.POST['username']
        contrasena = request.POST['password']
        usuario = authenticate(username=usuario, password = contrasena)
        if usuario is not None:
            login(request, usuario)
            return redirect('principal')

    contexto = {
        'formulario': formulario
    }
    return render(request, 'iniciarSesion/iniciarSesion2.html', context=contexto) 
    
@login_required
def perfil(request):
    return render(request, 'perfil/perfil.html')     