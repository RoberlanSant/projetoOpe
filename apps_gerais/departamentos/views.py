from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from django.urls import reverse_lazy

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        try:
            empresa_logada = self.request.user.funcionario.empresa
            return Departamento.objects.filter(empresa=empresa_logada)
        except Exception as e:
            return Departamento.objects.all()


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome','empresa']
    #Lembrar de verificar depois

    def form_valid(self, form):
        try:
            departamento = form.save(commit=False)
            departamento.empresa = self.request.user.funcionario.empresa
            departamento.save()
            return super(DepartamentoCreate, self).form_valid(form)
            
        except Exception as e:
            departamento = form.save(commit=False)
            departamento.save()
            return super(DepartamentoCreate, self).form_valid(form)



class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome','empresa']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')