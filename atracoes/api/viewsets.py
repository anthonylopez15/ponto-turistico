from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracoesViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('nome', 'descricao')
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
