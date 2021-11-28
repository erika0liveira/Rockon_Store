from django.shortcuts import render
from django.urls.converters import register_converter

def carrinho(request):
    return render(request, "carrinho/carrinho.html")
    