from __future__ import unicode_literals
from app.informacion.models import fichas
from django.db import models

from cStringIO import StringIO
import os

class nance_general(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	ed_maxi = models.FloatField()
	ed_mand = models.FloatField()

	def __unicode__(self):
		return '{}'.format(self.fichas)

class nance_tablas(models.Model):
    fichas = models.ForeignKey(fichas, null=False, blank=False, on_delete=models.CASCADE)
    seleccion = models.BooleanField()
    tabla = models.IntegerField()
    posicion = models.CharField(max_length=50)
    mdm = models.FloatField(null=True,blank=True)
    mprx = models.FloatField(null=True,blank=True)
    multiplicacion = models.FloatField(null=True,blank=True)
    mdrx = models.FloatField(null=True,blank=True)
    valor_x= models.FloatField(blank=False)

    def __unicode__(self):
    	return '{}'.format(self.fichas)


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
