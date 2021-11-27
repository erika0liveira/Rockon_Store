from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('perfil', perfil, name='perfil'),
    path('carrinho', carrinho, name='carrinho'),
]

