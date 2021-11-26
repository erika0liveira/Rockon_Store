from django.urls import path
from .views import index, item, buscar


urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('buscar', buscar, name='buscar'),
    path('<int:pk>/item', item, name='item'),
]
