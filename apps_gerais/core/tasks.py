# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from apps_gerais.funcionarios.models import Funcionario
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_relatorio():
		total = funcionarios.objects.all().count()
		send_email(
			'Relatório celery',
			'Relatorio Geral de funcionarios %f' % total,
			'<django@></django@>roberfalc@gmail.com',
			['contato@roberfalc@gmail.com'],
			fail_silently=False,
		)
		return True
