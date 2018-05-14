from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models


class Livro(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='livro_user',
        default=1)
    nome = models.CharField(
        "Nome",
        max_length=200)
    autor = models.CharField(
        "Autor",
        max_length=200)
    serie = models.CharField(
        "Série",
        max_length=200,
        blank=True,
        null=True)
    num_paginas = models.IntegerField(
        "Número de páginas",
        blank=True,
        null=True)
    inicio = models.DateField(
        "Começou em",
        blank=True,
        null=True)
    fim = models.DateField(
        "Terminou em",
        blank=True,
        null=True)
    nota = models.IntegerField(
        "Nota",
        blank=True,
        null=True)
    ebook = models.BooleanField("É um ebook")
    obs = models.TextField("Impressões", null=True, blank=True)

    class Meta:
        ordering = ['inicio']

    def __str__(self):
        return self.nome + ' - '+ self.autor

    def get_absolute_url(self):
        return reverse('livro:livro-list')
        
