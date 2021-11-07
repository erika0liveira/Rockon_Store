from django.shortcuts import get_object_or_404, get_list_or_404, render

def index(request):
    return render(request, 'index.html')


def item(request):
    item = get_object_or_404(item, pk=produto_id)
    return render(request, 'item.html')