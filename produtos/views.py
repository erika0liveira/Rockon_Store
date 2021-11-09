from django.shortcuts import render

from .models import Produto

def index(request):
    obj = Produto.objects.all()
    context = {'prods': obj}
    return render(request, "index.html", context)


def item(request):
    return render(request, 'item.html')

