from django.urls import path
from .views import listar_medicos
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos),
    path('consultas/nova/', views.criar_consulta),
]
