# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError


"""
Validação para não pertitir agendar datas retroativas
"""
def validate_date(data):
    if data <= timezone.now().date():
        raise ValidationError('%s Não é possivel afetuar um agendamento com data retroativa.' % data)


class Agenda(models.Model):
    data = models.DateField(validators=[validate_date])
    inicio = models.TimeField()
    fim = models.TimeField()
    paciente = models.CharField(max_length=128)
    procedimento = models.TextField()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % (self.paciente)

    """ Prepara url absoluta para o slug """
    def get_api_url(self):
        return reverse("api-agenda:detail", kwargs={"slug": self.slug})

    """ Trata plural e ordena objetos por data por ordem crecente """
    class Meta:
        verbose_name=u'Agenda'
        verbose_name_plural=u'Agendas'
        ordering = ['data']

""" Valida o slug automatico caso os dados sejam criados pela da API REST """
def create_slug(instance, new_slug=None):
    slug = slugify(instance.procedimento)
    if new_slug is not None:
        slug = new_slug
    qs = Agenda.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Agenda)
