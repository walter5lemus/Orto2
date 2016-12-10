from __future__ import unicode_literals
from django.db import models
from app.informacion.models import fichas
from app.analisis_radiograficos.choices import *


# Create your models here.

class aspectos_articulares(models.Model):
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	condilo_mand_izq_alto = models.FloatField()
	condilo_mand_izq_ancho = models.FloatField()
	condilo_mand_der_alto = models.FloatField()
	condilo_mand_der_ancho = models.FloatField()
	condilo_mand_simetrico = models.IntegerField(choices=simetrico_choices, default=1)
	condilo_mand_aspectos_observados = models.CharField(max_length=50)
	eminencia_izq = models.FloatField()
	eminencia_der = models.FloatField()
	eminencia_simetrico = models.IntegerField(choices=simetrico_choices, default=1)
	eminencia_aspectos_observados = models.CharField(max_length=50)
	espacio_articular_simetrico = models.IntegerField(choices=simetrico_choices, default=1)
	espacio_articular_aspectos_observados = models.CharField(max_length=50)

	def __unicode__(self):
		return '{}'.format(self.fichas)

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

#Otros Aspectos

BOOL_CHOICES = ((True, 'Simetria'), (False, 'Asimetria'))

class aspectos_mandibulares2(models.Model):

    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    aspectos_sinusales_simetrico = models.BooleanField(choices = BOOL_CHOICES, default=True)
    aspectos_sinusales_izq_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    aspectos_sinusales_der_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    ord_ori_simetrico = models.BooleanField(choices = BOOL_CHOICES, default=True)
    ord_ori_izq_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    ord_ori_der_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    fpgd_fpgi_simetrico = models.BooleanField(choices = BOOL_CHOICES, default=True)
    fpgd_fpgi_izq_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    fpgd_fpgi_der_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    veloc_erup_simetrico = models.BooleanField(choices = BOOL_CHOICES, default=True)
    veloc_erup_izq_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    veloc_erup_der_aspect_observ = models.CharField(max_length=20, blank=True, null=True)
    diagnostico = models.CharField(max_length=500, blank=False, null=False)
    
    def __unicode__(self):
        return '{}'.format(self.fichas)

#Otros Hallazgos

class estadios_de_nolla(models.Model):

    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    e_1_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_1_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_2_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_3_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    e_4_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    otros_hallazgos = models.CharField(max_length=200, blank=False, null=False)

    def __unicode__(self):
        return '{}'.format(self.fichas)

class secuencia_y_cronologia(models.Model):
    
    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    o_1_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_1_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_2_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_3_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_1 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_3 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_4 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_5 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_6 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_7 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    o_4_8 = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    
    def __unicode__(self):
        return '{}'.format(self.fichas)