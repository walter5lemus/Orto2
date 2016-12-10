from __future__ import unicode_literals
from app.informacion.models import fichas
from django.db import models

from cStringIO import StringIO
import os

class moyers_superior(models.Model):	

	fichas = models.ForeignKey(fichas,null=True, blank=True, on_delete=models.CASCADE)
	ed_izquierdo = models.FloatField(null=True, blank=True)
	ed_derecho = models.FloatField(null=True, blank=True)
	
	def __str__(self):
		return '{}'.format(self.fichas)

class pos(models.Model):

	def __unicode__(self):
		return '{}'.format(self.nombre_problemas)


class moyers_superior_ancho(models.Model):	

	fichas = models.ForeignKey(fichas,null=True, blank=True, on_delete=models.CASCADE)
	posicion = models.OneToOneField(pos,null=True, blank=True, unique=True)
	ancho_mesiodistal = models.FloatField(null=True, blank=True)
	
	def __str__(self):
		return '{}'.format(self.fichas)

class moyers_inferior(models.Model):
    fichas = models.ForeignKey(fichas, null=True, blank=True, on_delete=models.CASCADE)
    ed_izquierdo = models.FloatField(null=True, blank=True)
    ed_derecho = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.fichas)

class moyers_inferior_ancho(models.Model):
    fichas = models.ForeignKey(fichas, null=True, blank=True, on_delete=models.CASCADE)
    posicion = models.OneToOneField(pos, null=True, blank=True, unique=True)
    ancho_mesiodistal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.fichas)
