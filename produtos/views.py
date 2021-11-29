from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Produto, Categoria


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


class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Produto.available.all()

        categoria_slug = self.kwargs.get("slug")
        if categoria_slug:
            self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
            queryset = queryset.filter(categoria=self.categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["caterogia"] = self.categoria
        context["categorias"] = Categoria.objects.all()
        return context