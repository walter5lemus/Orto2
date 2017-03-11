from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas, datos_generales
from app.diagCefalo.choices import *

# Create your models here.

class diagnostico_cefalometrico(models.Model):

	#cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	patron_esqueletal = models.IntegerField(choices=patron_esqueletal_choices)
	tipo_de_crecimiento = models.IntegerField(choices=crecimiento_choices)
	medidas_dentales = models.IntegerField(choices=medidas_dentales_choices)

	otro_patron = models.CharField(max_length=100, blank=True, null=True)
	medidas_esteticas = models.TextField()

def __unicode__(self):
         return '{}'.format(self.fichas)
