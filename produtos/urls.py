from django.urls import path
from .views import index, item, Teste

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('<int:pk>/item', item, name='item'),
    # path('<int:pk>/item', Teste.as_view(), name='item'),
]

