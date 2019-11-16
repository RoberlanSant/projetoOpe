#import password as password
from django.views.generic import(ListView,
                                UpdateView,
                                DeleteView,
                                CreateView,
                                DetailView
)
from .models import Funcionario
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import View

from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa



class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        try:
            empresa_logada = self.request.user.funcionario.empresa
            return Funcionario.objects.filter(empresa=empresa_logada)
        except Exception as e:
            return Funcionario.objects.all()

class FuncionarioDetail(DetailView):
    model = Funcionario


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','cpf','idade','email','telefone',
    'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome','cpf','idade','email','telefone',
    'departamentos','empresa']

    def form_valid(self, form):
        try:
            funcionario = form.save(commit=False)
            username = funcionario.email
            funcionario.empresa = self.request.user.funcionario.empresa
            funcionario.user = User.objects.create(username=username)
            funcionario.password = User.objects.create(password=password)
            funcionario.save()
            return super(FuncionarioNovo, self).form_valid(form)
        except:
            funcionario = form.save(commit=False)
            username = funcionario.email
            #Depois precisa colocar algum validador 
            # ele dá erro com unique em relação ao nome de usuário por estár igual ao(não aceita dois emails iguais) email agora, mas só no envio
            funcionario.empresa = funcionario.empresa
            funcionario.user = User.objects.create(username=username)
            #funcionario.password = User.objects.create(password=password)
            #Ele não está importando password 
            funcionario.save()
            return super(FuncionarioNovo, self).form_valid(form)




# gerar relatório reportlab pesquisar para efetuar melhorias
def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatório de funcionarios')

    try:
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

    except:
        funcionarios = Funcionario.objects.all()
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

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html =template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] ='attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Erro Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')
