from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
