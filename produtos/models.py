from django.db import models
from autoslug import AutoSlugField


class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome_produto")
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    disponivel = models.BooleanField(default=True)
