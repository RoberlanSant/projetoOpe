from rest_framework import routers, serializers, viewsets
from apps_gerais.funcionarios.models import Funcionario
from apps_gerais.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer



class FuncionarioSerializer(serializers.ModelSerializer):
		registrohoraextra_set = RegistroHoraExtraSerializer(many=True)

		class Meta:
			model = Funcionario
			fields = ['id', 'nome', 'departamentos', 'empresa', 'user', 'imagem', 'total_horas_extra', 'registrohoraextra_set']
