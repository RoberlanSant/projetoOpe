from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        try:
            obj = form.save()
            funcionario = self.request.user.funcionario
            funcionario.empresa = obj
            funcionario.save()
            return super(EmpresaCreate, self).form_valid(form)
        except:
            obj = form.save()
            return super(EmpresaCreate, self).form_valid(form)


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']