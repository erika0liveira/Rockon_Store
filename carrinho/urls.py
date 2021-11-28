from django.urls import path
from .views import carrinho

# talvez incluir app name nos outros apps
app_name = "carrinho"

urlpatterns = [
    path("", carrinho, name="detalhes"),

]
