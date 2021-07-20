from django.http import response
from apps.producto.models import Producto
from .serializers import ProductoOrganizado
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productoObtenido(request):
    productos = Producto.objects.all()
    productosOrganizacion = ProductoOrganizado(productos, many = True)
    return Response(productosOrganizacion.data, 200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productoBuscado(request, id):
    juegos = None
    try:
        juegos = Producto.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None, status= 404)
    datos = ProductoOrganizado(juegos, many = False)
    return Response(datos.data, 200)
        

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productoAgregado(request):
    productoAgregados = ProductoOrganizado(data = request.data)
    if productoAgregados.is_valid():
        datos = productoAgregados.save()
        return Response(data = datos, status= 201)
    return Response(data = None, status = 403)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productoModificado(request, id):
    productoInsertado = Producto.objects.get(pk = id)
    if productoInsertado == None:
        return Response(data = None, status = 404)
    productoObtener = ProductoOrganizado(instance = productoInsertado, data = request.data)
    if productoObtener.is_valid():
        editada = productoObtener.save()
        return Response(data = editada, status = 200)
    return Response(data = None, status = 403)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def productoBorrado(request, id):
    productoObtener = Producto.objects.get(pk = id)
    if productoObtener == None:
        return Response(data = None, status = 404)
    productoObtener.delete()
    return Response(data = None, status = 200)      