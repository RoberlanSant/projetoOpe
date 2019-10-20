from django.db import models
from django.urls import reverse_lazy
from django.core import validators
from django.core.exceptions import ValidationError


def validate_even(value):
    if len(value) != 8:
        raise ValidationError(('Em %(value)s. Faltam dígitos')
        ,params={'value': value},)
    for n in value:
        try:
           n=int(n) 
        except:
            raise ValidationError(('Em %(value)s. Algum valor inserido não é um número')
            ,params={'value': value},)
                

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM',max_length=8, validators=[validate_even], unique=True)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)

    class Meta:
        ordering = ('produto',)
    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }