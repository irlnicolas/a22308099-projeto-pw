from django.shortcuts import render
from .models import Genero, Filme, Ator

def view_filmes(request):
    filmes = Filme.objects.all()
    generos = Genero.objects.all()
    return render(request, "filmes.html", {"filmes": filmes, "generos": generos})

def view_filme(request, nome):
    filme = Filme.objects.get(nome=nome)
    atores = Ator.objects.filter(filme__nome=nome)
    return render(request, "filme.html", {"filme":filme, "atores": atores})