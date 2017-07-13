# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from app.gestorImg.forms import *
from app.gestorImg.models import *
from django.views.generic import TemplateView
from django.core import serializers

from app.informacion.models import *

codi="0000-00"

def index(request):
	return render(request, 'aspectos/index.html')

def img_paciente_crear(request,codi,num):
	str(codi)
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		if img_paciente.objects.filter(fichas_id=ids.id).exists() and img_paciente2.objects.filter(fichas_id=ids.id).exists():
			imagenes = img_paciente.objects.get(fichas_id=ids.id)
			imagenes2 = img_paciente2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = PacienteForm(instance=imagenes)
				form2 = PacienteForm2(instance=imagenes2)
			else:
				form = PacienteForm(request.POST, request.FILES, instance=imagenes)
				form2 = PacienteForm2(request.POST, request.FILES, instance=imagenes2)
				if form.is_valid() and form2.is_valid():
					form.save()
					form2.save()
				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/nuevo/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/paciente_crear.html', {'form':form,'form2':form2,'codi':codi,'num':num})	
		else:
			if request.method == 'POST':
				form = PacienteForm(request.POST, request.FILES,initial={'fichas':ids.id})
				form2 = PacienteForm2(request.POST, request.FILES,initial={'fichas':ids.id})
				if form.is_valid() and form2.is_valid():
					form.save()
					form2.save()
				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/nuevo/%s/%s/'%(codi,num))
			else:
				form = PacienteForm(initial={'fichas':ids.id})
				form2 = PacienteForm2(initial={'fichas':ids.id})
		return render(request, 'gestorImg/paciente_crear.html', {'form':form,'form2':form2,'num':num,'codi':codi})

def img_paciente_editar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			imagenes = img_paciente.objects.get(fichas_id=ids.id)
			imagenes2 = img_paciente2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = PacienteForm(instance=imagenes)
				form2 = PacienteForm2(instance=imagenes2)
			else:
				form = PacienteForm(request.POST, request.FILES, instance=imagenes)
				form2 = PacienteForm2(request.POST, request.FILES, instance=imagenes2)
				if form.is_valid() and form2.is_valid():
					form.save()
					form2.save()
				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/editar/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/paciente_editar.html', {'form':form,'form2':form2,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def img_paciente_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			imagenes = img_paciente.objects.get(fichas_id=ids.id)
			imagenes2 = img_paciente2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form= PacienteForm_consultar(instance=imagenes)
				form2= PacienteForm_consultar2(instance=imagenes2)
			else: 
				form= PacienteForm_consultar(request.POST, request.FILES, instance=imagenes)
				form2= PacienteForm_consultar2(request.POST, request.FILES, instance=imagenes2)
				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/consultar/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/paciente_consultar.html', {'form':form,'form2':form2,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

class MostrarPaciente(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				imagepx = img_paciente.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', imagepx, fields=('pfacial','pfrontal','psonrisa','osuperior','oinferior','lizquierdo','lderecho','frontal'))
		return HttpResponse(data, content_type='application/json')

class MostrarPaciente2(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				imagepx2 = img_paciente2.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', imagepx2, fields=('pfacial2','pfrontal2','psonrisa2','osuperior2','oinferior2','lizquierdo2','lderecho2','frontal2'))
		return HttpResponse(data, content_type='application/json')