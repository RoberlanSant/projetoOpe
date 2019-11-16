from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps_gerais.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        try:
            super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
            self.fields['funcionario'].queryset = Funcionario.objects.filter(
                empresa=user.funcionario.empresa)
        except:
            super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
            self.fields['funcionario'].queryset = Funcionario.objects.all()
               


    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']