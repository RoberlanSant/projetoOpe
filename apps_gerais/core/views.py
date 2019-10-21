from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps_gerais.funcionarios.models import Funcionario
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps_gerais.core.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from .tasks import send_relatorio
from django.db.models import Sum
from .tasks import send_relatorio



@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionario = request.user.funcionario
    data['total_funcionarios'] = funcionario.empresa.total_funcionarios
    data['total_funcionarios_ferias'] = funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_ok'] = funcionario.empresa.total_funcionarios_doc_ok
    data['total_funcionarios_doc_pendente'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_funcionarios_rg'] = 10
    data['total_funcionarios_doc_pendente'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_hora_extra_utilizadas'] = RegistroHoraExtra.objects.filter(
    	funcionario__empresa=funcionario.empresa, utilizada=True).aggregate(Sum('horas'))['horas__sum']
    data['total_hora_extra_pendente'] = RegistroHoraExtra.objects.filter(
    	funcionario__empresa=funcionario.empresa, utilizada=False).aggregate(Sum('horas'))['horas__sum']
    return render(request, 'core/index.html', data)


def celery(request):
		send_relatorio.delay()
		return HttpResponse('Tarefa incluida na fila para execução')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
