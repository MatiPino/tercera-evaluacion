from django.http import request
from django.shortcuts import render, redirect
from .forms import RegistroUsuario
# Create your views here.
def registro(request):
    formulario = None
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            usuario.save()
            return redirect('base')
    if request.method == 'GET':
        formulario = RegistroUsuario()
    contexto = {
        'formulario': formulario
    }            
    return render(request, 'registrar/registro.html', context= contexto)