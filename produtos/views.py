from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Produto

def index(request):
    obj = Produto.objects.all()
    context = {'prods': obj}
    return render(request, "index.html", context)


def item(request, pk):
    teste = {'teste': Produto.objects.get(id=pk)}
    return render(request, 'item.html', teste)

class Teste(generic.DetailView):
    model = Produto
    template_name = 'item.html'
    def get_queryset(self):
        return Produto.objects.all()
    
