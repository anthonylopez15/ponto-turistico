
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentariosViewSet
from enderecos.api.viewsets import EnderecosViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'enderecos', EnderecosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
