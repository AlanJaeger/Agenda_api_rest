# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Agenda
from django.utils import timezone

class AgendaViewsTestCase200(TestCase):
    def test_request200(self):
        response = self.client.get('/agenda/')
        self.assertEqual(response.status_code, 200)

class AgendaViewsTestCase404(TestCase):
    def test_request404(self):
        response = self.client.get('/agendas/')
        self.assertEqual(response.status_code, 404)
