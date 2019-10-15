from django.views.generic import(ListView,
                                UpdateView,
                                DeleteView,
                                CreateView
)
from .models import Funcionario
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome',
    'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)




# gerar relatório reportlab pesquisar para efetuar melhorias
def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatório de funcionarios')

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s   |Hora extra: %.2f'

    p.drawString(0, 800, '_'*150)

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ %(funcionario.nome, funcionario.total_horas_extra))
        y -= 20

    p.showPage()
    p.save


    pdf =buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
