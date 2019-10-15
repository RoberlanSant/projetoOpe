from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit,
                    HoraExtraEditGeral,
                    HoraExtraDelete,
                    HoraExtraUpdate,
                    UtilizouHoraExtra
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horas-extras'),
    path('novo/', HoraExtraUpdate.as_view(), name='create_horas-extras'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_horas-extras'),
    path('editar/<int:pk>/', HoraExtraEditGeral.as_view(), name='update_horas-extras_geral'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora-extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horas-extras'),
]
