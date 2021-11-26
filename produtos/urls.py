from django.urls import path
from .views import index, item

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('<int:pk>/item', item, name='item'),
]
