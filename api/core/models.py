from django.db import models

# Create your models here
class Empresas(models.Model):
    nome = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__ (self):
        return self.nome