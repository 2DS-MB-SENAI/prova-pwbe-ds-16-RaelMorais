from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('servicos/', views.api_servicos, name="GET e POST serviços"),
    path('servicos/<int:pk>', views.servico_por_id, name="Serviço por ID"), 

    path('agendamentos/', views.api_agendamentos, name="Criar agendamento"),
    path('agendamentos/<int:pk>', views.agendamento_por_id, name="Agendamento por ID"),
]
