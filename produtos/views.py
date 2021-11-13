from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Produto

def index(request):
    context = {'prods': Produto.objects.all()}
    return render(request, "index.html", context)


def item(request, pk):
    context = {'item': Produto.objects.get(id=pk)}
    return render(request, 'item.html', context)
