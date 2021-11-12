from django.contrib import admin
from django.db.models.fields import BooleanField
from .models import Produto


class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'categoria', 'preco', 'disponivel')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('nome_produto', )
    list_filter = ('categoria', )
    list_editable = ('disponivel', )
    list_per_page = 10


admin.site.register(Produto, ListandoProdutos)