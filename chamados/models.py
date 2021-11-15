from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)

class Chamado(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField()

