# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from agenda.models import Agenda

# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['paciente']
    prepopulated_fields = {'slug': ('paciente',)}

admin.site.register(Agenda,AgendaAdmin)
