from django.shortcuts import render
from .models import Banda, Album, Musica

# Create your views here.
def view_bandas(request):
    bandas = Banda.objects.all()
    return render(request, "index.html", {"bandas": bandas})

def view_banda(request, nome):
    banda = Banda.objects.get(nome=nome)
    albuns = Album.objects.filter(banda__nome=nome)
    return render(request, "banda.html", {"banda": banda, "albuns": albuns})

def view_album(request, titulo):
    album = Album.objects.get(titulo=titulo)
    musicas = Musica.objects.filter(album__titulo=titulo)
    return render(request, "album.html", {"album": album, "musicas": musicas})

def view_musica(request, titulo):
    musica = Musica.objects.get(titulo=titulo)
    return render(request, "musica.html", {"musica": musica})