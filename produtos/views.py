from django.shortcuts import render
from .models import Produto

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
                nome_produto__contains = termo,
                disponivel = True,
            )

            context = {'produtos_encontrados' : busca_produtos}
            return render(request, 'produtos/busca.html', context)

        # Definir algo para quando não houver um termo
        else:
            pass