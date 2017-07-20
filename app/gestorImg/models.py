# -*- coding: utf-8 -*
#!/usr/bin/env python

from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas
from app.aspectos.choices import *
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class img_paciente(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	pfacial = models.ImageField(upload_to='paciente/pfacial/',blank=True,null=True)
	pfrontal = models.ImageField(upload_to='paciente/pfrontal/',blank=True,null=True)
	psonrisa = models.ImageField(upload_to='paciente/psonrisa/',blank=True,null=True)
	osuperior = models.ImageField(upload_to='paciente/osuperior/',blank=True,null=True)
	oinferior = models.ImageField(upload_to='paciente/oinferior/',blank=True,null=True)
	lizquierdo = models.ImageField(upload_to='paciente/lizquierdo/',blank=True,null=True)
	lderecho = models.ImageField(upload_to='paciente/lderecho/',blank=True,null=True)
	frontal = models.ImageField(upload_to='paciente/frontal/',blank=True,null=True)

	def __str__(self):
		return '{}'.format(self.fichas)

class img_paciente2(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	pfacial2 = models.ImageField(upload_to='paciente/pfacial/',blank=True,null=True)
	pfrontal2 = models.ImageField(upload_to='paciente/pfrontal/',blank=True,null=True)
	psonrisa2 = models.ImageField(upload_to='paciente/psonrisa/',blank=True,null=True)
	osuperior2 = models.ImageField(upload_to='paciente/osuperior/',blank=True,null=True)
	oinferior2 = models.ImageField(upload_to='paciente/oinferior/',blank=True,null=True)
	lizquierdo2 = models.ImageField(upload_to='paciente/lizquierdo/',blank=True,null=True)
	lderecho2 = models.ImageField(upload_to='paciente/lderecho/',blank=True,null=True)
	frontal2 = models.ImageField(upload_to='paciente/frontal/',blank=True,null=True)

	def __str__(self):
		return '{}'.format(self.fichas)

class img_radiograficas(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	ipano = models.ImageField(upload_to='radiograficas/inicial/',blank=True,null=True)
	icefa = models.ImageField(upload_to='radiograficas/inicial/',blank=True,null=True)
	tpano = models.ImageField(upload_to='radiograficas/trazados/',blank=True,null=True)
	tcefa = models.ImageField(upload_to='radiograficas/trazados/',blank=True,null=True)
	spano = models.ImageField(upload_to='radiograficas/seguimiento/',blank=True,null=True)
	scefa = models.ImageField(upload_to='radiograficas/seguimiento/',blank=True,null=True)
	
	def __str__(self):
		return '{}'.format(self.fichas)

class img_modelo(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	osupm = models.ImageField(upload_to='modelo/osuperior/',blank=True,null=True)
	oinfm = models.ImageField(upload_to='modelo/oinferior/',blank=True,null=True)
	lizqm = models.ImageField(upload_to='modelo/lizquierdo/',blank=True,null=True)
	frontm = models.ImageField(upload_to='modelo/frontal/',blank=True,null=True)
	lderm = models.ImageField(upload_to='modelo/lderecho/',blank=True,null=True)
	
	def __str__(self):
		return '{}'.format(self.fichas)

class img_aparato(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	aparatof = models.ImageField(upload_to='aparato/frontal/',blank=True,null=True)
	aparatol= models.ImageField(upload_to='aparato/lateral/',blank=True,null=True)
	aparato = models.ImageField(upload_to='aparato/arriba/',blank=True,null=True)

	def __str__(self):
		return '{}'.format(self.fichas)


