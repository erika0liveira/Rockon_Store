from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from model_utils.models import TimeStampedModel

class Categoria(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produtos:list_by_categoria", kwargs={"slug": self.slug})

class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria, related_name="produtos", on_delete=models.CASCADE
    )
    nome_produto = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome_produto")
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    disponivel = models.BooleanField(default=True)


    class Meta:
            ordering = ("nome_produto",)

    def __str__(self):
            return self.nome_produto

