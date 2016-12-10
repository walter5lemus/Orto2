from __future__ import unicode_literals
from django.db import models
from app.aspMandibular.choices import *
from app.informacion.models import fichas, datos_generales

# Create your models here.

class diagnostico_general(models.Model):

	cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)

	diagnostico_ortodontico_general = models.TextField()
	problemas = models.TextField()
	objetivos = models.TextField()
	tratamiento = models.IntegerField(choices=Tratamiento)
	descripcion_tratamiento = models.TextField()
	
def __unicode__(self):
         return '{}'.format(self.diagnostico_general)
