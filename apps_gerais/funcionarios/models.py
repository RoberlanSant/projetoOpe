from django.db import models
from django.contrib.auth.models import User
from apps_gerais.departamentos.models import Departamento
from apps_gerais.empresa.models import Empresa
from django.urls import reverse
from django.db.models import Sum

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField('CPF', max_length=11, unique=True)
	idade = models.IntegerField()
	email = models.EmailField(unique=True)
	telefone = models.CharField(max_length=20, blank=True)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	departamentos = models.ManyToManyField(Departamento)
	empresa = models.ForeignKey(
		Empresa, on_delete=models.PROTECT, null=True, blank=True)
	imagem = models.ImageField()
	de_ferias = models.BooleanField(default=False)


	def get_absolute_url(self):
		return reverse('home')

	@property
	def total_horas_extra(self):
		total = self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
		return total or 0



	def __str__(self):
		return self.nome
