from django.db import models

# Create your models here.


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    imgCapaUrl = models.CharField(max_length=300)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

