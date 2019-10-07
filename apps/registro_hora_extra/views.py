from .models import RegistroHoraExtra
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm
from django.contrib.auth.models import User
from django.views.generic import(ListView, 
                                UpdateView, 
                                DeleteView, 
                                CreateView
)


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
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