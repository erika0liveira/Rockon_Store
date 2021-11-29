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

        for item in carrinho.values():
            item["preco"] = Decimal(item["preco"])
            item["total"] = item["quantidade"] * item["preco"]
            item["atualiza_quantidade_form"] = CarrinhoAddProdutoForm(
                initial={"quantidade": item["quantidade"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantidade"] for item in self.carrinho.values())

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
            Decimal(item["preco"]) * item["quantidade"] for item in self.carrinho.values()
        )

    def save(self):
        self.session.modified = True