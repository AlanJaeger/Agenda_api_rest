# -*- coding: utf-8 -*-
from __future__ import unicode_literals
""" Importando views uma para cada função """
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from agenda.models import Agenda
""" Importação com curinga (*), uso de todas as Views Menos codigo"""
from .serializer import *


class AgendaCreatelAPIView(CreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaCreateSerializer


class AgendaDetailAPIView(RetrieveAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailsSerializer
    lookup_field = 'slug'


class AgendaUpdateAPIView(UpdateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailsSerializer
    lookup_field = 'slug'


class AgendaDeleteAPIView(DestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailsSerializer
    lookup_field = 'slug'


class AgendaListAPIVew(ListAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaListSerializer
