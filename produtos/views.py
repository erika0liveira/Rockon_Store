from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Produto
from carrinho.forms import CarrinhoAddProdutoForm
from django.views.generic import DetailView

def index(request):
    context = {'produtos': Produto.objects.all()}
    return render(request, "produtos/index.html", context)


def item(request, pk):
    context = {'item': Produto.objects.get(id=pk)}
    return render(request, 'produtos/item.html', context)


def busca(request):
    
    # Verifica se o request trouxe o termo de busca
    if 'termo' in request.GET:
        termo = request.GET['termo']
        # Verifica se o termo de busca tem algum valor para busca
        if termo != '':
            print(termo)
            # Realizando a busca no banco de dados
            busca_produtos = Produto.objects.order_by('-preco').filter(
                nome_produto__icontains = termo,
                disponivel = True,
            )

            context = {'produtos_encontrados' : busca_produtos}
            return render(request, 'produtos/busca.html', context)

        # Definir algo para quando não houver um termo
        else:
            pass

    
def ProdutoDetailView(DetailView):
    QuerySet = Produto.available.all()
    extra = {"form": CarrinhoAddProdutoForm()}