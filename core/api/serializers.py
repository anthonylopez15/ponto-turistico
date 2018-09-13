from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from core.models import PontoTuristico, DocIdentificacao
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa', 'descricao_completa2', 'doc_identificacao'
        )

        read_only_fields = ('comentarios',)

    def cria_atracoe(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        avaliacoes = validated_data['avaliacoes']
        del validated_data['avaliacoes']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoe(atracoes, ponto)

        ponto.avaliacoes.set(avaliacoes)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
