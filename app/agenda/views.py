# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from agenda.models import Agenda


def portfolio_exibir(request):

    agendas = Agenda.objects.filter()
    content = {
        'agendas':agendas,
    }

    return render(request,'agenda/agenda.html', content)
