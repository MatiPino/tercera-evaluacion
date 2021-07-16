from django.http import response
from apps.carrito.models import Total
from .serializers import CarritoOrganizado
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
def carritoObtenido(request):
    carro = Total.objects.all()
    carritoOrganizacion = CarritoOrganizado(carro, many = True)
    return Response(carritoOrganizacion.data, 200)

@api_view(['GET'])
def carritoBuscado(request, id):
    carrito = None
    try:
        carrito = Total.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None, status= 404)
    datos = CarritoOrganizado(carrito, many = False)
    return Response(datos.data, 200)
        
@api_view(['POST'])
def carritoAgregado(request):
    carritoAgregados = CarritoOrganizado(data = request.data)
    if carritoAgregados.is_valid():
        datos = carritoAgregados.save()
        return Response(data = datos, status= 201)
    return Response(data = None, status = 403)

@api_view(['DELETE'])
def carritoBorrado(request, id):
    carritoObtener = Total.objects.get(pk = id)
    if carritoObtener == None:
        return Response(data = None, status = 404)
    carritoObtener.delete()
    return Response(data = None, status = 200)  