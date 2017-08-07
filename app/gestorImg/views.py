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
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
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
					return HttpResponseRedirect('/gestor_img/radiograficas/nuevo/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/paciente_crear.html', {'form':form,'form2':form2,'codi':codi,'num':num, 'nombreUser':nombreUser})	
			else:
				if request.method == 'POST':
					form = PacienteForm(request.POST, request.FILES,initial={'fichas':ids.id})
					form2 = PacienteForm2(request.POST, request.FILES,initial={'fichas':ids.id})
					if form.is_valid() and form2.is_valid():
						form.save()
						form2.save()
					return HttpResponseRedirect('/gestor_img/radiograficas/nuevo/%s/%s/'%(codi,num))
				else:
					form = PacienteForm(initial={'fichas':ids.id})
					form2 = PacienteForm2(initial={'fichas':ids.id})
			return render(request, 'gestorImg/paciente_crear.html', {'form':form,'form2':form2,'num':num,'codi':codi, 'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})


def img_paciente_editar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	if request.user.rol==1:
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
					return HttpResponseRedirect('/gestor_img/radiograficas/editar/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/paciente_editar.html', {'form':form,'form2':form2,'codi':codi,'num':num, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})



def img_paciente_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

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
				return HttpResponseRedirect('/gestor_img/radiograficas/consultar/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/paciente_consultar.html', {'form':form,'form2':form2,'codi':codi,'num':num,'usuario_creador':ids.usuario_creador.username, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	


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



def img_radiograficas_crear(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
				imagenes = img_radiograficas.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = RadiograficasForm(instance=imagenes)
				else:
					form = RadiograficasForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/modelo/nuevo/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/radiograficas_crear.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})	
			else:
				if request.method == 'POST':
					form = RadiograficasForm(request.POST, request.FILES,initial={'fichas':ids.id})
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/modelo/nuevo/%s/%s/'%(codi,num))
				else:
					form = RadiograficasForm(initial={'fichas':ids.id})
			return render(request, 'gestorImg/radiograficas_crear.html', {'form':form,'num':num,'codi':codi, 'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})

def img_radiograficas_editar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	if request.user.rol==1:
		pass
		try:
			ids = fichas.objects.get(cod_expediente=codi,numero=num)
			if ids:
				imagenes = img_radiograficas.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = RadiograficasForm(instance=imagenes)
				else:
					form = RadiograficasForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/modelo/editar/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/radiograficas_editar.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})

def img_radiograficas_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			imagenes = img_radiograficas.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form= RadiograficasForm_consultar(instance=imagenes)
			else: 
				form= RadiograficasForm_consultar(request.POST, request.FILES, instance=imagenes)
				return HttpResponseRedirect('/gestor_img/modelo/consultar/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/radiograficas_consultar.html', {'form':form,'codi':codi,'num':num,'usuario_creador':ids.usuario_creador.username, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	

class MostrarRadiograficas(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				image = img_radiograficas.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', image, fields=('ipano','icefa','tpano','tcefa','spano','scefa'))
		return HttpResponse(data, content_type='application/json')

def img_modelo_crear(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			if img_modelo.objects.filter(fichas_id=ids.id).exists():
				imagenes = img_modelo.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = ModeloForm(instance=imagenes)
				else:
					form = ModeloForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/aparato/nuevo/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/modelo_crear.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})	
			else:
				if request.method == 'POST':
					form = ModeloForm(request.POST, request.FILES,initial={'fichas':ids.id})
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/aparato/nuevo/%s/%s/'%(codi,num))
				else:
					form = ModeloForm(initial={'fichas':ids.id})
			return render(request, 'gestorImg/modelo_crear.html', {'form':form,'num':num,'codi':codi, 'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})

def img_modelo_editar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	if request.user.rol == 1:
		try:
			ids = fichas.objects.get(cod_expediente=codi,numero=num)
			if ids:
				imagenes = img_modelo.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = ModeloForm(instance=imagenes)
				else:
					form = ModeloForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/gestor_img/aparato/editar/%s/%s/' %(codi,num))
				return render(request, 'gestorImg/modelo_editar.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})

def img_modelo_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			imagenes = img_modelo.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form= ModeloForm_consultar(instance=imagenes)
			else: 
				form= ModeloForm_consultar(request.POST, request.FILES, instance=imagenes)
				return HttpResponseRedirect('/gestor_img/aparato/consultar/%s/%s/' %(codi,num))
			return render(request, 'gestorImg/modelo_consultar.html', {'form':form,'codi':codi,'num':num,'usuario_creador':ids.usuario_creador.username, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	

class MostrarModelo(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				image = img_modelo.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', image, fields=('osupm','oinfm','lizqm','frontm','lderm'))
		return HttpResponse(data, content_type='application/json')

def img_aparato_crear(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			if img_aparato.objects.filter(fichas_id=ids.id).exists():
				imagenes = img_aparato.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = AparatoForm(instance=imagenes)
				else:
					form = AparatoForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/home/')
				return render(request, 'gestorImg/aparato_crear.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})	
			else:
				if request.method == 'POST':
					form = AparatoForm(request.POST, request.FILES,initial={'fichas':ids.id})
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/%s/'%(codi,num))
				else:
					form = AparatoForm(initial={'fichas':ids.id})
			return render(request, 'gestorImg/aparato_crear.html', {'form':form,'num':num,'codi':codi, 'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})

def img_aparato_editar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	if request.user.rol==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi,numero=num)
			if ids:
				imagenes = img_aparato.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = AparatoForm(instance=imagenes)
				else:
					form = AparatoForm(request.POST, request.FILES, instance=imagenes)
					if form.is_valid():
						form.save()
					return HttpResponseRedirect('/home/')
				return render(request, 'gestorImg/aparato_editar.html', {'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})

def img_aparato_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			imagenes = img_aparato.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form= AparatoForm_consultar(instance=imagenes)
			else: 
				form= AparatoForm_consultar(request.POST, request.FILES, instance=imagenes)
				return HttpResponseRedirect('/home/')
			return render(request, 'gestorImg/aparato_consultar.html', {'form':form,'codi':codi,'num':num,'usuario_creador':ids.usuario_creador.username, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	

class MostrarAparato(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				image = img_aparato.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', image, fields=('aparatof','aparatol','aparato'))
		return HttpResponse(data, content_type='application/json')