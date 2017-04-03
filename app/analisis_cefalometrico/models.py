from __future__ import unicode_literals
from app.informacion.models import fichas
from django.db import models

from cStringIO import StringIO
import os


class examen(models.Model):

	def __unicode__(self):
		return '{}'.format(self.id)


class analisis_cefalometrico(models.Model):	
	fichas = models.ForeignKey(fichas,null=True, blank=True, on_delete=models.CASCADE)
	numero_de_examen = models.ForeignKey(examen,null=True, blank=True) 
	sna = models.FloatField(null=True, blank=True)
	snb = models.FloatField(null=True, blank=True)
	anb = models.FloatField(null=True, blank=True)
	convexidad  = models.FloatField(null=True, blank=True)
	wits = models.FloatField(null=True, blank=True)
	long_cuerpo_mandibular = models.FloatField(null=True, blank=True)
	profundidad_maxilar = models.FloatField(null=True, blank=True)
	profundidad_facial = models.FloatField(null=True, blank=True)
	plano_mandibular = models.FloatField(null=True, blank=True)
	eje_y_fh = models.FloatField(null=True, blank=True)
	cono_facial = models.FloatField(null=True, blank=True)
	eje_facial = models.FloatField(null=True, blank=True)
	angulo_goniaco_superior = models.FloatField(null=True, blank=True)
	angulo_goniaco_inferior = models.FloatField(null=True, blank=True)
	angulo_goniaco_total = models.FloatField(null=True, blank=True)
	is_na = models.FloatField(null=True, blank=True)
	is_sn = models.FloatField(null=True, blank=True)
	isfh = models.FloatField(null=True, blank=True)
	impa = models.FloatField(null=True, blank=True)
	protusion_de_incisivo_max = models.FloatField(null=True, blank=True)
	protusion_de_incisivo_md = models.FloatField(null=True, blank=True)
	protusion_labial = models.FloatField(null=True, blank=True)
	def __str__(self):
		return '{}'.format(self.fichas)
