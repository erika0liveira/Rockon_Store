from django.urls import path
from . import views
from .views import index, item

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('item.html', item, name='item'),
    # path('', teste_produto, name='index'),
]