from rest_framework import serializers
from .models import CustomUser

# Criando o serializer para retornar os dados do banco como JSON
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
