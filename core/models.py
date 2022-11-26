from django.db import models

class product(models.Model):
    nome = models.CharField(max_length=100)
    quant = models.IntegerField()
    price = models.CharField(max_length=100)
    categ = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class categ(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class client(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    nasc = models.CharField(max_length=100)
    card = models.CharField(max_length=3)
    def __str__(self):
        return self.nome

