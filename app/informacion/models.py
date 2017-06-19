# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from app.informacion.choices import *
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
# Create your models here.

class Usuario(AbstractUser):
    dui = models.CharField(max_length=10,null=True, blank=True)
    carnet = models.CharField(max_length=7,null=True, blank=True)


###################################################################################

class datos_generales(models.Model):
    cod_expediente = models.CharField(max_length=10, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    edad_registro = models.IntegerField()
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    genero = models.IntegerField(choices=genero_choices, default=1)
    direccion = models.CharField(max_length=200)
    nombre_resp = models.CharField(max_length=100)
    usuario_creador = models.ForeignKey(Usuario,null=False, blank=False)
    fecha_hora_creacion = models.DateTimeField()
    departamento = models.IntegerField()

    def __unicode__(self):
        return '{}'.format(self.cod_expediente)



class fichas(models.Model):
    cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.IntegerField()
    usuario_creador = models.ForeignKey(Usuario,null=False, blank=False)
    completada = models.IntegerField()

    class Meta:
        unique_together = [("cod_expediente", "numero")]
        ordering = ['cod_expediente']


    def __unicode__(self):
        return  '{} {} '.format(self.cod_expediente,self.numero)

class ultima_modificacion(models.Model):
    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField() 
    

    def __unicode__(self):
        return '{}'.format(self.fichas)


class catalogo_enfermedades(models.Model):
    id_enfermedad = models.IntegerField(primary_key=True)
    nombre_enfermedad = models.CharField(max_length=30)

    def __unicode__(self):
        return  '{} {}'.format(self.id_enfermedad,self.nombre_enfermedad)

class motivo_consulta(models.Model):
    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    motivo_consulta = models.CharField(max_length=500)
    fechaRegistro = models.DateField(default=timezone.now()) 
    curso = models.IntegerField(choices=curso_choices,default=1)
    rotacion = models.IntegerField(choices=rotacion_choices,default=1)
    turno = models.IntegerField(choices=turnos_choices,default=1)

    def __unicode__(self):
        return '{}'.format(self.fichas)




class estado_general(models.Model):
    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    cambio_salud = models.BooleanField(choices=YES_OR_NO,default=False, null=False)
    detalle_enf_operacion = models.CharField(max_length=500, blank=True, null=True)
    detalle_medicamento = models.CharField(max_length=30, blank=True, null=True)
    detalle_otra_enfermedad = models.CharField(max_length=30,null=True,blank=True)
    otras_enfermedades = models.ManyToManyField(catalogo_enfermedades,null=True,blank=True)
    
    def __unicode__(self):
        return '{}'.format(self.fichas)

