from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    atracao = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'atracao',
            'endereco', 'aprovado', 'foto', 'descricao_completa',
            'descricao_completa2'
        )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
