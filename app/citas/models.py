from __future__ import unicode_literals
from app.informacion.models import *
from app.citas.choices import *
from django.db import models
from django.template.defaultfilters import date

# Create your models here.

class citas(models.Model):
	fichas = models.ForeignKey(fichas, null=False, blank=False, on_delete=models.CASCADE)
	num_cita = models.IntegerField()
	fecha_cita = models.DateField() 
	observaciones= models.CharField(max_length=250)
	proxima_cita =  models.DateField() 	
	resultados = models.CharField(max_length=250)
	autorizacion = models.BooleanField()
	tutor = models.CharField(max_length=250,null=False, blank=False)

	def __unicode__(self):
		return '{} {}'.format(self.codigo,self.num_cita)

class citas_general(models.Model):
	fichas = models.ForeignKey(fichas, null=False, blank=False, on_delete=models.CASCADE)
	aparato = models.IntegerField(choices=aparato_choices) 
	mx = models.BooleanField()
	md = models.BooleanField()
	estudiante = models.ForeignKey(Usuario,null=False, blank=False)

	def __unicode__(self):
		return '{} {}'.format(self.codigo,self.aparato)