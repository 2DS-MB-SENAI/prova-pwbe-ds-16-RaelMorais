from rest_framework import serializers
from .models import Agendamento, Servico

# Criando o serializer para retornar os dados do banco como JSON
class AgendamentoSerializer(serializers.ModelSerializer):
    data_hora = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Agendamento
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
