from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)

