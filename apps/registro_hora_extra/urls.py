from django.urls import path
from .views import (HoraExtraList#, 
                    #HoraExtraEdit, 
                    #HoraExtraDelete,
                    #HoraExtraUpdate
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horas-extras'),
    #path('novo/', HoraExtraUpdate.as_view(), name='create_horas-extras'),
    #path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_horas-extras'),
    #path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horas-extras'),
]