from rest_framework import routers, serializers, viewsets
from apps_gerais.registro_hora_extra.models import RegistroHoraExtra




class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']

