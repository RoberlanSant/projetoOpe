from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps_gerais.funcionarios.api.views import FuncionarioViewSet
from apps_gerais.registro_hora_extra.api.views import RegistroHoraExtraViewSet
from rest_framework import routers
from apps_gerais.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/registro_hora_extra', RegistroHoraExtraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += i18n_patterns (
    path('', include('apps_gerais.core.urls')),
    path('funcionarios/', include('apps_gerais.funcionarios.urls')),
    path('departamentos/', include('apps_gerais.departamentos.urls')),
    path('documentos/', include('apps_gerais.documentos.urls')),
    path('empresa/', include('apps_gerais.empresa.urls')),
    path('horas-extras/', include('apps_gerais.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('produto/', include('apps_gerais.produto.urls')),
    path('estoque/', include('apps_gerais.estoque.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
