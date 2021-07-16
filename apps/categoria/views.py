from django.shortcuts import render
from .models import Categoria
from .forms import FormularioCategoria
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def categoria(request):
    formularioC = FormularioCategoria()
    if request.method == 'POST':
        formularioC = FormularioCategoria(request.POST)
        if formularioC.is_valid():
            formularioC.save()
    context = {'formulario': formularioC,
               'titulo': 'Agregar Categoria'}

    return render(request, 'agregar/producto.html', context)     