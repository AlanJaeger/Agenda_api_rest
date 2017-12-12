# coding: utf-8
from django.conf.urls import url
""" Importação com curinga (*), uso de todas as Views Menos codigo"""
from .views import *


urlpatterns = [
    url(r'^agenda/$', AgendaListAPIVew.as_view(), name='list'),
    url(r'^agenda/create/$', AgendaCreatelAPIView.as_view(), name='create'),
    url(r'^agenda/(?P<slug>[\w-]+)/$', AgendaDetailAPIView.as_view(), name='detail'),
    url(r'^agenda/(?P<slug>[\w-]+)/update/$', AgendaUpdateAPIView.as_view(), name='update'),
    url(r'^agenda/(?P<slug>[\w-]+)/delete/$', AgendaDeleteAPIView.as_view(), name='delete'),
]
