from django.http import response
from apps.categoria.models import Categoria
from .serializers import CategoriaOrganizada
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
def categoriaObtenida(request):
    categorias = Categoria.objects.all()
    categoriasOrganizacion = CategoriaOrganizada(categorias, many = True)
    return Response(categoriasOrganizacion.data, 200)

@api_view(['GET'])
def categoriaBuscada(request, id):
    categoria = None
    try:
        categoria = Categoria.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None, status= 404)
    datos = CategoriaOrganizada(categoria, many = False)
    return Response(datos.data, 200)
        
@api_view(['POST'])
def categoriaAgregada(request):
    categoriaAgregadas = CategoriaOrganizada(data = request.data)
    if categoriaAgregadas.is_valid():
        datos = categoriaAgregadas.save()
        return Response(data = datos, status= 201)
    return Response(data = None, status = 403)

@api_view(['DELETE'])
def categoriaBorrada(request, id):
    categoriaObtener = Categoria.objects.get(pk = id)
    if categoriaObtener == None:
        return Response(data = None, status = 404)
    categoriaObtener.delete()
    return Response(data = None, status = 200)              