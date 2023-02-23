from django.shortcuts import render
from .models import Genero, Filme


def home(request):
    generos = Genero.objects.all()
    filmes = Filme.objects.all()
    return render(request, 'home.html', {'generos': generos, 'filmes': filmes})


def getFilmesPorGenero(request, id):
    genero = Genero.objects.get(id=id)
    generos = Genero.objects.all()
    filmes = Filme.objects.filter(genero=genero)

    return render(request, 'filmes.html', {'id': id, 'genero': genero, 'filmes': filmes, 'generos': generos})
