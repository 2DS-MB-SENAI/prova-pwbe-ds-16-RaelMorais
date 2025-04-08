from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Agendamento, Servico
from .serializers import AgendamentoSerializer, ServicoSerializer
from rest_framework import status

@api_view(['GET', 'POST']) # Get para retornar todos os dados dos serviços se o metodod for GET e se for POST criar 
def api_servicos(request):
    if request.method == 'GET': 
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# api get para retornar os dados de serviço, filtrado por ID. 
def servico_por_id(request, pk):
    try:
        servicos = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response({'Error':'Serviço não existe.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServicoSerializer(servicos)
    return Response(serializer.data)


          



@api_view(['GET', 'POST']) # Get para retornar todos os dados de agendamentos se for GET ou criar se for POST
def api_agendamentos(request):
    if request.method == 'GET': 
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) # Pesquisa agendamento por ID 
def agendamento_por_id(request, pk):
    try:
        agendamento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:  
        return Response({'Error':'Agendamento não existe.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AgendamentoSerializer(agendamento)  
    return Response(serializer.data)

## 2 gets e 1 post, 1 get geral, 1 post e 1 get por ID
# Create your views here.
