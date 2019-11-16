from django.http import HttpResponse
import json
import csv
import xlwt
from .models import RegistroHoraExtra
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import(ListView,
                                UpdateView,
                                DeleteView,
                                CreateView
)


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        try:
            empresa_logada = self.request.user.funcionario.empresa
            return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        except Exception as e:   
            return RegistroHoraExtra.objects.all()

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditGeral(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    #success_url = reverse_lazy('update_horas-extras_geral')

    def get_success_url(self):
        return reverse_lazy('update_horas-extras_geral', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditGeral, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horas-extras')


class HoraExtraUpdate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado =self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Requisição executada',
             'horas': float(empregado.total_horas_extra)
             }
        )
        return HttpResponse(response, content_type='application/json')


class ExportarCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_re = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas'])

        for registro in registro_re:
            writer.writerow([registro.id, registro.motivo, registro.funcionario,
             registro.funcionario.total_horas_extra, registro.horas])

        return response



class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros =RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response
