from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .carrinho import Carrinho


@require_POST
def carrinho_add(request, produto_id):
    print(f'View carrinho_add: {request.POST}')
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    
    carrinho.add(
           produto=produto, quantidade=1, override_quantity=False,
        )
       
    return redirect("carrinho:carrinho")


@require_POST
def carrinho_remove(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remove(produto)
    return redirect("carrinho:carrinho")


def carrinho(request):

    print(f'View carrinho: {request.POST}')

    carrinho = Carrinho(request)
    return render(request, "carrinho/carrinho.html", {"carrinho": carrinho})
    