from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='nome da empresa')

    def __str__(Self):
        return self.nome