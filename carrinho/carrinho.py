import copy
from decimal import Decimal
from django.conf import settings
from produtos.models import Produto
from .forms import CarrinhoAddProdutoForm


class Carrinho:
    def __init__(self, request):
        if request.session.get(settings.CARRINHO_SESSION_ID) is None:
            request.session[settings.CARRINHO_SESSION_ID] = {}

        self.carrinho = request.session[settings.CARRINHO_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        carrinho = copy.deepcopy(self.carrinho)

        produtos = Produto.objects.filter(id__in=carrinho)
        for produto in produtos:
            carrinho[str(produto.id)]["produto"] = produto

        for produto in carrinho.values():
            produto["preco"] = Decimal(produto["preco"])
            produto["total"] = produto["quantidade"] * produto["preco"]
            produto["atualiza_quantidade_form"] = CarrinhoAddProdutoForm(
                initial={"quantidade": produto["quantidade"], "override": True}
            )

            print(produto["produto"])
            yield produto

    def get_total_preco(self):
        total = 0
        for produto in self.carrinho.values():
            produto["preco"] = Decimal(produto["preco"])
            produto["total"] = produto["quantidade"] * produto["preco"]
            total += produto["total"]
        return total

    def __len__(self):
        return sum(produto["quantidade"] for produto in self.carrinho.values())

    def add(self, produto, quantidade=1, override_quantity=False):
        produto_id = str(produto.id)
    
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {
                "quantidade": 0,
                "preco": str(produto.preco),
            }
      
        if override_quantity:
            self.carrinho[produto_id]["quantidade"] = quantidade
        else:
            self.carrinho[produto_id]["quantidade"] += quantidade
    
        self.carrinho[produto_id]["quantidade"] = min(20, self.carrinho[produto_id]["quantidade"])
    
        self.save()


    def remove(self, produto):
        produto_id = str(produto.id)

        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()

    def total(self):
        return sum(
            Decimal(produto["preco"]) * produto["quantidade"] for produto in self.carrinho.values()
        )

    def save(self):
        self.session.modified = True