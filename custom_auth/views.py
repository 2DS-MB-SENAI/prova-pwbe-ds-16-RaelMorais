from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
import re




@api_view(['POST'])
# Endpoit para criação de usuario 


def create_user_credentials(request):
    username = request.data.get('username')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address = request.data.get('address')
    birth_date = request.data.get('birth_date')

    if not username or not password or not phone:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST) # rertornando status codes. 
    
    if CustomUser.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    password = str(password)
    # password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # if not re.match(password_regex, password):
    #     return Response({
    #         'Erro': 'A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial.'
    #     }, status=status.HTTP_400_BAD_REQUEST)

    user = CustomUser.objects.create_user(

        username=username,
        password=password,
        phone=phone,
        address = address, 
        birth_date = birth_date, 

    )

    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)


# endpoint para requisição de token 
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso':str(refresh.access_token),
            'refresh': str(refresh),

        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou/e senha incorreto'}, status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_user(request):
    usuario = request.user 
    serializer = CustomUserSerializer(usuario)
    return Response(serializer.data)
    
# Create your views here.
