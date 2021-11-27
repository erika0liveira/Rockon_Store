from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('busca', busca, name='busca'),
    path('<int:pk>/item', item, name='item'),
]
