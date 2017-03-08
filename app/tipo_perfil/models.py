# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas
from app.tipo_perfil.choices import *

# Create your models here.


class TipoPerfil(models.Model):

	#id_tipo_perfil = models.CharField(max_length=10, primary_key=True)	
	#cod_expediente = models.ForeignKey(FacialFrontal, null=True, blank=True, on_delete=models.CASCADE)

	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	frontal_facial = models.IntegerField(choices=facial_frontal_choices)
	tipoPerfiltotal = models.IntegerField(choices=perfil_total_choices)
	perfilTercio_inferior = models.IntegerField(choices=ptercio_inferior_choices)
	tipoSonrisa = models.IntegerField(choices=sonrisa_choice)
	tipo_competenciaLabial = models.IntegerField(choices=competencia_labial_choices)
	grosorLabios= models.IntegerField(choices=labios_grosor_choices)
	tamanoLabios = models.IntegerField(choices=tamano_labios_choices)

	tipoNariz = models.IntegerField(choices=tipo_nariz_choices)
	angulo_Naso_labial = models.IntegerField()
	tercio_superior = models.IntegerField()
	tercio_medio = models.IntegerField()
	tercio_inferior = models.IntegerField()
	tamanoSonrisa = models.IntegerField()



	def __unicode__(self):
         return '{}'.format(self.fichas)

		

