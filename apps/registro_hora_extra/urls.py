from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit,
                    HoraExtraEditGeral,
                    HoraExtraDelete,
                    HoraExtraUpdate,
                    UtilizouHoraExtra,
                    ExportarCSV,
                    ExportarExcel
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horas-extras'),
    path('novo/', HoraExtraUpdate.as_view(), name='create_horas-extras'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_horas-extras'),
    path('editar/<int:pk>/', HoraExtraEditGeral.as_view(), name='update_horas-extras_geral'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora-extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horas-extras'),
    path('exportar-csv/', ExportarCSV.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarExcel.as_view(), name='exportar_excel'),
]
