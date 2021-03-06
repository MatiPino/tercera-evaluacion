from django.http import response
from rest_framework import permissions
from apps.categoria.models import Categoria
from .serializers import CategoriaOrganizada
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def categoriaObtenida(request):
    categorias = Categoria.objects.all()
    categoriasOrganizacion = CategoriaOrganizada(categorias, many = True)
    return Response(categoriasOrganizacion.data, 200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def categoriaBuscada(request, id):
    categoria = None
    try:
        categoria = Categoria.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None, status= 404)
    datos = CategoriaOrganizada(categoria, many = False)
    return Response(datos.data, 200)
        
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def categoriaAgregada(request):
    categoriaAgregadas = CategoriaOrganizada(data = request.data, many = False)
    if categoriaAgregadas.is_valid():
        datos = categoriaAgregadas.save()
        categoriaAgregadas = CategoriaOrganizada(datos, many = False)
        return Response(data = categoriaAgregadas.data, status= 201)
    return Response(data = categoriaAgregadas.errors, status = 403)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def categoriaBorrada(request, id):
    categoriaObtener = Categoria.objects.get(pk = id)
    if categoriaObtener == None:
        return Response(data = None, status = 404)
    categoriaObtener.delete()
    return Response(data = None, status = 200)              