from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    data_inclusao = models.DateField()
    descricao = models.TextField()
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome

