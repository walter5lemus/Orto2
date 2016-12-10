from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas, datos_generales

# Create your models here.

class diagnostico_cefalometrico(models.Model):

	cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)

	patron_esqueletal = models.TextField()
	tipo_de_crecimiento = models.TextField()
	medidas_dentales = models.TextField()
	medidas_esteticas = models.TextField()

def __unicode__(self):
         return '{}'.format(self.diagnostico_cefalometrico)
