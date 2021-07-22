from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['POST'])
def iniciar_sesion(request):
        
    username = request.data ['username']
    password = request.data ['password'] 
    usuarioEncontrado = authenticate(username= username, password= password)
    if usuarioEncontrado is not None:
        datos = {}
        tokenCreado = Token.objects.create(user= usuarioEncontrado)
        datos['token'] = tokenCreado.key
        return Response(data = datos, status= 200)
    return Response(data = request.data, status=403)