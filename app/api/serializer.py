# coding: utf-8

from rest_framework.serializers import ModelSerializer, DateTimeField, HyperlinkedIdentityField
from agenda.models import Agenda


"""
Hyperlink para interações com JSON direto no link List, Delete e Update
"""

agenda_list_url = HyperlinkedIdentityField(
        view_name='api-agenda:detail',
        lookup_field='slug'
        )

agenda_delete_url = HyperlinkedIdentityField(
        view_name='api-agenda:delete',
        lookup_field='slug'
        )

agenda_update_url = HyperlinkedIdentityField(
        view_name='api-agenda:update',
        lookup_field='slug'
        )

"""
Tres de Serializer cada uma com suas particularidades
ocultando ou exibindos fields
"""
class AgendaListSerializer(ModelSerializer):
    """ Formata data padrão UTF-8 """
    data = DateTimeField(format='%d-%m-%Y')
    """ Hiperlink para listar agenda """
    url = agenda_list_url
    class Meta:
        model = Agenda
        fields = ['data','inicio','fim','paciente', 'procedimento','url']

        def __unicode__(self):
            return '%s' % (self.paciente)

class AgendaDetailsSerializer(ModelSerializer):
    delete = agenda_delete_url
    update = agenda_update_url
    data = DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = Agenda
        fields = ['id','data','inicio','fim','paciente', 'procedimento','delete', 'update']

        def __unicode__(self):
            return '%s' % (self.paciente)

class AgendaCreateSerializer(ModelSerializer):

    class Meta:
        model = Agenda
        fields = ['data','inicio','fim','paciente', 'procedimento']

        def __unicode__(self):
            return '%s' % (self.paciente)
