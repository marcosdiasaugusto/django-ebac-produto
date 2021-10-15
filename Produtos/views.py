from django.shortcuts import render, get_object_or_404
from .models import Produto

def lista(request):
    lista_de_produtos = Produto.objects.all()

    return render(request, 
                'lista_produtos.html',
                {'lista': lista_de_produtos})

def pega_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)

    return render(request,
    "mostra_produto.html",
    {'produto': produto})

