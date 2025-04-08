from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/', views.create_user_credentials, name="registrar usuario"),
    path('login/', views,login_user, name="logar"), 
]
