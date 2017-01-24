#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas
from app.denticion.choices import *
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os


# Create your models here.
#######################
#Decime si ves esto plox 
###########################

class problema(models.Model):
	nombre_problemas = models.CharField(max_length=20)

	def __unicode__(self):
		return '{}'.format(self.nombre_problemas)

problema1 = problema(id=1,nombre_problemas="Pérdidas prematuras")
problema1.save()
problema2 = problema(id=2,nombre_problemas="Anodoncias")
problema2.save()
problema3 = problema(id=3,nombre_problemas="Mordida telescópica")
problema3.save()

class registro(models.Model):
	fichas = models.ForeignKey(fichas, null=False, blank=False, on_delete=models.CASCADE)
	problema = models.ForeignKey(problema, null=False, blank=False, on_delete=models.CASCADE)
	cuadrante = models.IntegerField(null=True, blank=True)
	pieza = models.IntegerField(null=True, blank=True)
	detalle = models.CharField(null=True, blank=True, max_length=30)

	def __unicode__(self):
		return '{}'.format(self.fichas, self.problema)

class tipo(models.Model):
	nombre = models.CharField(max_length=10)

	def __unicode__(self):
		return '{}'.format(self.nombre)

tipo1 = tipo(id=1,nombre="Temporario")
tipo1.save()
tipo2 = tipo(id=2,nombre="Mixto")
tipo2.save()
tipo3 = tipo(id=3,nombre="Permanente")
tipo3.save()

class denticion(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	tipo = models.OneToOneField(tipo, null=False, blank=False, on_delete=models.CASCADE, default=2)
	diastemas = models.CharField(max_length=50)
	mal_posiciones = models.CharField(max_length=50)
	supernumerarios = models.CharField(max_length=50)
	tejido_intraorales = models.CharField(max_length=200)
	encias = models.CharField(max_length=100)
	frenillos = models.CharField(max_length=100)
	lengua = models.CharField(max_length=100)
	observaciones_generales = models.CharField(max_length=384)

	def __unicode__(self):
		return '{}'.format(self.fichas)

class linea_media_facial(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	mx = models.IntegerField(choices=mx_md_choices)
	mx_desviacion = models.IntegerField(choices=desviaciones_choices)
	md = models.IntegerField(choices=mx_md_choices)
	md_desviacion = models.IntegerField(choices=desviaciones_choices)

	def __str__(self):
		return '{}'.format(self.fichas)

class sobremordidas(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	horizontal = models.IntegerField(choices=sobremordidas_choices)
	vertical = models.IntegerField(choices=sobremordidas_choices)

	def __str__(self):
		return '{}'.format(self.fichas)

class registro_mordidas(models.Model):
	fichas = models.ForeignKey(fichas, null=False, blank=False, on_delete=models.CASCADE)
	cuad_superior = models.IntegerField()
	pieza_superior = models.IntegerField()
	cuad_inferior = models.IntegerField()
	pieza_inferior = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.fichas)

class relaciones_sagitales(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	molar_derecha = models.IntegerField(choices=molar_canina_choices, default=1)
	molar_izquierda = models.IntegerField(choices=molar_canina_choices, default=1)
	canina_derecha = models.IntegerField(choices=molar_canina_choices, default=1)
	canina_izquierda = models.IntegerField(choices=molar_canina_choices, default=1)
	plano_termina_recto = models.IntegerField(choices=plano_escalon_choices, default=1)
	escalon_mesial = models.IntegerField(choices=plano_escalon_choices, default=1)
	escalon_distal = models.IntegerField(choices=plano_escalon_choices, default=1)
	observaciones = models.TextField()

	def __str__(self):
		return '{}'.format(self.fichas)

class funcion_mandibular(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	apertura = models.IntegerField()
	desv_afmp_derecho = models.IntegerField()
	desv_afmp_izquierdo = models.IntegerField()
	signos_sintomas_atm = models.TextField()

	def __str__(self):
		return '{}'.format(self.fichas)

class imagenes_afmp(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	nombreimagen = models.CharField(max_length=50, default='Sin nombre')
	imagen = models.ImageField(upload_to='afmp',blank=True,null=True)

	def __str__(self):
		return '{}'.format(self.fichas)
