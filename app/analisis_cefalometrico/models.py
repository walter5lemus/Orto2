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
	sna = models.FloatField()
	snb = models.FloatField()
	anb = models.FloatField()
	convexidad  = models.FloatField()
	wits = models.FloatField()
	long_cuerpo_mandibular = models.FloatField()
	profundidad_maxilar = models.FloatField()
	profundidad_facial = models.FloatField()
	plano_mandibular = models.FloatField()
	eje_y_fh = models.FloatField()
	cono_facial = models.FloatField()
	eje_facial = models.FloatField()
	angulo_goniaco_superior = models.FloatField()
	angulo_goniaco_inferior = models.FloatField()
	angulo_goniaco_total = models.FloatField()
	is_na = models.FloatField()
	is_sn = models.FloatField()
	isfh = models.FloatField()
	impa = models.FloatField()
	protusion_de_incisivo_max = models.FloatField()
	protusion_de_incisivo_md = models.FloatField()
	protusion_labial = models.FloatField()
	def __str__(self):
		return '{}'.format(self.fichas)
