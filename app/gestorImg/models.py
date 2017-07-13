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

		
