from django.shortcuts import render
from .models import Produto

def index(request):
    context = {'produtos': Produto.objects.all()}
    return render(request, "index.html", context)


def item(request, pk):
    context = {'item': Produto.objects.get(id=pk)}
    return render(request, 'item.html', context)


def buscar(request):
    busca_produto = Produto.objects.order_by('-preco').filter(disponivel=True)
    print(request.GET)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if buscar:
            busca_produto = busca_produto.filter(nome_produto__icontains=nome_buscar)
            
            
   
    dados = {
        'produtos': busca_produto,
    }

    return render(request, 'buscar.html', dados)