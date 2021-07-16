from django.http import response
from apps.cuentas.models import Perfil
from .serializers import PerfilOrganizado
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
def perfilObtenido(request):
    perfiles = Perfil.objects.all()
    perfilesOrganizacion = PerfilOrganizado(perfiles, many = True)
    return Response(perfilesOrganizacion.data, 200)

@api_view(['GET'])
def perfilBuscado(request, id):
    perfil = None
    try:
        perfil = Perfil.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None, status= 404)
    datos = PerfilOrganizado(perfil, many = False)
    return Response(datos.data, 200)
        

@api_view(['POST'])
def perfilAgregado(request):
    perfilesAgregados = PerfilOrganizado(data = request.data)
    if perfilesAgregados.is_valid():
        datos = perfilesAgregados.save()
        return Response(data = datos, status= 201)
    return Response(data = None, status = 403)

@api_view(['PUT'])
def perfilModificado(request, id):
    perfilInsertado = Perfil.objects.get(pk = id)
    if perfilInsertado == None:
        return Response(data = None, status = 404)
    perfilObtener = PerfilOrganizado(instance = perfilInsertado, data = request.data)
    if perfilObtener.is_valid():
        editada = perfilObtener.save()
        return Response(data = editada, status = 200)
    return Response(data = None, status = 403)

@api_view(['DELETE'])
def perfilBorrado(request, id):
    perfilObtener = Perfil.objects.get(pk = id)
    if perfilObtener == None:
        return Response(data = None, status = 404)
    perfilObtener.delete()
    return Response(data = None, status = 200)   