from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas, datos_generales

# Create your models here.

class Patron(models.Model):
	id_Patron = models.CharField(max_length=10, primary_key=True)
	patron_esqueletal = models.CharField(max_length=50)

	def __unicode__(self):
         return '{}'.format(self.patron_esqueletal)



class Crecimiento(models.Model):
	id_Crecimiento = models.CharField(max_length=10, primary_key=True)
	tipo_de_crecimiento = models.CharField(max_length=50)

	def __unicode__(self):
         return '{}'.format(self.tipo_de_crecimiento)



class MDentales(models.Model):
	id_MDentales = models.CharField(max_length=10, primary_key=True)
	medidas_dentales = models.CharField(max_length=50)

	def __unicode__(self):
         return '{}'.format(self.medidas_dentales)



class diagnostico_cefalometrico(models.Model):

	#cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	patron_esqueletal = models.ForeignKey(Patron, null=True, blank=True, on_delete=models.CASCADE)
	tipo_de_crecimiento = models.ForeignKey(Crecimiento, null=True, blank=True, on_delete=models.CASCADE)
	medidas_dentales = models.ForeignKey(MDentales, null=True, blank=True, on_delete=models.CASCADE)

	otro_patron = models.CharField(max_length=100, blank=True, null=True)
	medidas_esteticas = models.TextField()

def __unicode__(self):
         return '{}'.format(self.fichas)
