from __future__ import unicode_literals
from django.db import models
from app.aspMandibular.choices import *
from app.informacion.models import fichas, datos_generales

# Create your models here.

class aspectos_mandibulares1(models.Model):

	cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)

	rama_mand_anch_izq_altura = models.IntegerField()
	rama_mand_anch_der_altura = models.IntegerField()
	rama_mand_anch_simetrico = models.IntegerField(choices=Simetria, null=False, blank=False)
	rama_mand_anch_izq_aspect_observ = models.TextField()
	rama_mand_anch_der_aspect_observ = models.TextField()

	rama_mand_altur_izq_altura = models.IntegerField()
	rama_mand_altur_der_altura = models.IntegerField()
	rama_mand_altur_simetrico = models.IntegerField(choices=Simetria, null=False, blank=False)
	rama_mand_altur_izq_aspect_observ = models.TextField()
	rama_mand_altur_der_aspect_observ = models.TextField()


	cuerpo_mand_altur_izq_altura = models.IntegerField()
	cuerpo_mand_altur_der_altura = models.IntegerField()
	cuerpo_mand_altur_simetrico = models.IntegerField(choices=Simetria, null=False, blank=False)
	cuerpo_mand_altur_izq_aspect_observ = models.TextField()
	cuerpo_mand_altur_der_aspect_observ = models.TextField()

	cuerpo_mand_long_izq_altura = models.IntegerField()
	cuerpo_mand_long_der_altura = models.IntegerField()
	cuerpo_mand_long_simetrico = models.IntegerField(choices=Simetria, null=False, blank=False)
	cuerpo_mand_long_izq_aspect_observ = models.TextField()
	cuerpo_mand_long_der_aspect_observ = models.TextField()

def __unicode__(self):
         return '{}'.format(self.aspectos_mandibulares1)
