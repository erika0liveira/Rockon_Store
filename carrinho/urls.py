from django.urls import path
from .views import carrinho, carrinho_add, carrinho_remove

# talvez incluir app name nos outros apps
app_name = "carrinho"

urlpatterns = [
    path("", carrinho, name="carrinho"),
    path("carrinho_add/<int:produto_id>/", carrinho_add, name="add"),
    path("carrinho_remove/<int:produto_id>/", carrinho_remove, name="remove"),
]
