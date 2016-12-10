from __future__ import unicode_literals
from app.reportes.models import *
from django.db import models
from app.informacion.models import fichas, datos_generales
# Create your models here.

class reportes(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	codigo = models.CharField(max_length=7)
	numero = models.IntegerField()

	def __unicode__(self):
		return '{}'.format(self.codigo)
