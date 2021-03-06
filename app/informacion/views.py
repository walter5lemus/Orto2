# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from collections import OrderedDict
from django.views.generic import TemplateView
from app.informacion.models import *
from app.informacion.forms import *
from django.core import serializers
from django.http import HttpResponse
import json
import time
import string
from django.db.models import Q



from app.analisis_cefalometrico.models import *
from app.analisis_radiograficos.models import *
from app.AnalisisDenticionMixta.models import *
from app.aspMandibular.models import *
from app.aspectos.models import *
from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.informacion.models import *
from app.tipo_perfil.models import *
codi=""

def CodExpediente_crear(request):
	user = request.user.id
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.method == 'POST':
		form = DatosGeneralesForm(request.POST)
		codi = form.data['codigo'] 
		if form.is_valid():
		 	form.save()
	else:
		incompletos =list()
		ficha = fichas.objects.filter(usuario_creador=user, completada=0)
		for fi in ficha:
			incompletos.append(fi.numero)
			incompletos.append(fi.cod_expediente)
			for fi in ficha:
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-5)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-6)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-7)	
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-9)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
			
		form = DatosGeneralesForm()
		return render(request, 'informacion/form_inicio.html', {'form':form,'incompletos':incompletos, 'nombreUser':nombreUser})


class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		cod = list(datos_generales.objects.filter(cod_expediente=codigo))
		data = serializers.serialize('json', cod)
		return HttpResponse(data, content_type='application/json')


class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		try:
			fi=fichas.objects.filter(cod_expediente=codigo)
			for ficha in fi:
				ids= fichas.objects.get(cod_expediente_id=ficha.cod_expediente_id,numero=ficha.numero, usuario_creador_id=request.user.id)
			fi=list(fichas.objects.filter(cod_expediente=codigo))
			data = serializers.serialize('json', fi, fields=('numero','completada'))
			return HttpResponse(data, content_type='application/json')
		except Exception, e:
			return HttpResponse('Error', status=401)


class BusquedaAjaxView22(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		fi=list(fichas.objects.filter(cod_expediente=codigo))
		data = serializers.serialize('json', fi, fields=('numero','completada'))
		return HttpResponse(data, content_type='application/json')


class BusquedaAjaxView22_editar(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		fi=list(fichas.objects.filter(Q(cod_expediente=codigo),Q(completada=0)|Q(completada=1)))
		data = serializers.serialize('json', fi, fields=('numero','completada'))
		return HttpResponse(data, content_type='application/json')


class BusquedaAjaxView22_retiro(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']


		fi=list(fichas.objects.filter(cod_expediente=codigo,completada=0))
		data = serializers.serialize('json', fi, fields=('numero','completada'))
		return HttpResponse(data, content_type='application/json')


def busqueda(request):
	if request.is_ajax():
		resultado = datos_generales.objects.filter(nombre_completo__istartswith= request.GET['nombre'] ).values('nombre_completo', 'cod_expediente')
		return HttpResponse( json.dumps( list(resultado)), content_type='application/json')


def busqueda2(request):
	if request.is_ajax():
		resultado = fichas.objects.filter(cod_expediente_id__cod_expediente__istartswith=request.GET['codigo']).values('cod_expediente').distinct()
		return HttpResponse( json.dumps( list(resultado)), content_type='application/json')


def busqueda_admin(request):
	if request.user.rol==1:
		if request.is_ajax():
			resultado = datos_generales.objects.filter(nombre_completo__istartswith= request.GET['nombre'] ).values('nombre_completo', 'cod_expediente')
			return HttpResponse( json.dumps( list(resultado)), content_type='application/json')


def busqueda2_admin(request):
	if request.user.rol==1:
		if request.is_ajax():
			resultado = fichas.objects.filter(cod_expediente_id__cod_expediente__startswith=request.GET['codigo']).values('cod_expediente').distinct()
			return HttpResponse( json.dumps( list(resultado)), content_type='application/json')


class busquedaCodigo(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		if fichas.objects.filter(cod_expediente=codigo).exists():
			cod = datos_generales.objects.filter(cod_expediente=codigo)
			data = serializers.serialize('json', cod, fields=('cod_expediente'))
			return HttpResponse(data, content_type='application/json')
		return HttpResponse("")


def CodExpediente_consular(request):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	form = DatosGeneralesForm()
	return render(request, 'informacion/form_inicio_consultar.html', {'form':form, 'nombreUser':nombreUser})



def CodExpediente_editar(request):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.method == 'POST':
		form = DatosGeneralesForm(request.POST)
		codi = form.data['codigo'] 
		if form.is_valid():
		 	form.save()
 			return HttpResponseRedirect('/informacion/estado_general/editar/%s/' %codi)
	 	else:
 			return HttpResponseRedirect('/informacion/estado_general/editar/%s/' %codi)
	else:
			form = DatosGeneralesForm()

			return render(request, 'informacion/form_inicio_editar.html', {'form':form, 'nombreUser':nombreUser})

###############################################################################

def DatosGeneral_crear(request):
	user = request.user.id
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	num = 1
	if request.method == 'POST':
			form = DatosGeneralesForm(request.POST)
			codi = request.POST.get('cod_expediente')
			if form.is_valid():	
			 	form.save()
				return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/%s' %(codi,num))
			else:
				return render(request, 'informacion/form_datosGenerales.html', {'form':form,'num':num, 'nombreUser':nombreUser})
	else:
			form = DatosGeneralesForm(initial={'usuario_creador':request.user.id})
	return render(request, 'informacion/form_datosGenerales.html', {'form':form,'num':num, 'nombreUser':nombreUser})


def DatosGeneral_crear2(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
						incompletos.append(-2)
						incompletos.append(-3)			
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm(instance=datos)
			else: 
				form = DatosGeneralesForm(request.POST, instance=datos)
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/%s' %(codi,num))
				else:
					return render(request,'informacion/form_datosGenerales2.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
			return render(request,'informacion/form_datosGenerales2.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")



def DatosGenerales_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	#try:
	ids = datos_generales.objects.get(cod_expediente=codi)
	if ids:
		incompletos =list()
		ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
		for fi in ficha:
			if not datos_generales.objects.filter(cod_expediente=codi).exists():
				incompletos.append(0)
			if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-1)
			if not estado_general.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-2)
			if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-3)
			if not registro.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-4)
			if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-5)
			if not registro.objects.filter(fichas_id=fi.id).exists():
				if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
					incompletos.append(-6)
			if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-7)	
			if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-8)
			if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-9)
			if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-10)
			if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-11)
			if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-12)
			if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-13)
			if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-14)
			if not nance_general.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-15)
			if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-16)
			if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-17)
			if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
				incompletos.append(-18)

		datos = datos_generales.objects.get(cod_expediente=codi)
		if request.method == 'GET':
			form = DatosGeneralesForm_consultar(instance=datos,initial={'usuario_creador':str(datos.usuario_creador)})
		else: 
			form = DatosGeneralesForm_consultar(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/informacion/motivo_consultas/consultar/%s/%s/' %(codi,num))

		return render(request,'informacion/form_datosGenerales_consultar.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
	return HttpResponse("No se encontro el Codigo de Expediente")
	#except Exception, e:
	#	return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})



def DatosGenerales_consultar2(request,codi):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm_consultar(instance=datos)
			else: 
				form = DatosGeneralesForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/' %codi)
			return render(request,'informacion/form_datosGenerales_existente.html',{'form':form,'codi':codi,'num':num, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})


def DatosGenerales_edit(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		#try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not datos_generales.objects.filter(cod_expediente=codi).exists():
					incompletos.append(0)
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-5)
						incompletos.append(-6)
						incompletos.append(-7)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-9)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-19)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-20)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-21)
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm(instance=datos)
			else: 
				form = DatosGeneralesForm(request.POST, instance=datos)
				if form.is_valid():
					co = request.POST.get('cod_expediente')
					form.save()
				return HttpResponseRedirect('/informacion/motivo_consultas/editar/%s/%s' %(codi,num))
			return render(request,'informacion/form_datosGenerales_editar.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		#except Exception, e:
		#	return HttpResponse("No se encontro el Codigo de Expediente")
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})

################################################################################################

def Motivo_Consulta_crear(request,codi,num):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if int(num)==1:
		if not fichas.objects.filter(cod_expediente_id=codi,numero=1).exists():
			fichas.objects.create(cod_expediente_id=codi, numero=1, usuario_creador_id=request.user.id,completada=0)
	else:
		try:
			ficha = fichas.objects.get(cod_expediente_id=codi,numero=int(num)-1)
			if ficha.completada !=0:
				if not fichas.objects.filter(cod_expediente_id=codi,numero=num).exists():
					fichas.objects.create(cod_expediente_id=codi, numero=num, usuario_creador_id=request.user.id,completada=0)
		except Exception as e:
			raise e
	try:
		fecha =  timezone.now()
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		incompletos =list()
		ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
		for fi in ficha:
			if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
					incompletos.append(-2)
					incompletos.append(-3)

		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			if motivo_consulta.objects.filter(fichas_id=ids.id).exists():
				if ids:
					estado = motivo_consulta.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						form = MotivoConsultaForm(instance=estado)
					else: 
						form = MotivoConsultaForm(request.POST, instance=estado)
						if form.is_valid():
							form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
							return redirect('/informacion/estado_general/nuevo/%s/%s/' %(codi,num))
						else:
							return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
					return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
				return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
			else:
				fecha =  timezone.now()
				if ultima_modificacion.objects.filter(fichas_id=ids.id).exists():{}
				else:
					ultima_modificacion.objects.create(fichas_id=ids.id,fecha=fecha)
				if request.method == 'POST':
					form = MotivoConsultaForm(request.POST)
					if form.is_valid():
					 	form.save()
						return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/%s' %(codi,num))
					else:
						return render(request, 'informacion/form_motivoconsulta.html', {'form':form,'codi': codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
				else:
					form = MotivoConsultaForm(initial={'fichas':ids.id,'fecha_hora_creacion':fecha})
					return render(request, 'informacion/form_motivoconsulta.html', {'form':form,'codi': codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_tiene_permiso.html', {'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	


def Motivo_Consulta_editar2(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			if ids:
				incompletos =list()
				ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
				for fi in ficha:
					if not datos_generales.objects.filter(cod_expediente=codi).exists():
						incompletos.append(0)
					if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
					if not estado_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-2)
					if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-3)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-4)
					if not registro.objects.filter(fichas_id=fi.id).exists():
							incompletos.append(-5)
							incompletos.append(-6)
							incompletos.append(-7)
					if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-8)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
							incompletos.append(-9)
					if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-10)
					if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-11)
					if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-12)
					if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-13)
					if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-14)
					if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-15)
					if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-16)
					if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-17)
					if not nance_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-18)
					if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-19)
					if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-20)
					if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-21)
				estado = motivo_consulta.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = MotivoConsultaForm(instance=estado)
				else: 
					form = MotivoConsultaForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
					return redirect('/informacion/estado_general/editar/%s/%s/' %(codi,num))
				return render(request,'informacion/form_motivoconsulta_editar1.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})


def Motivo_Consulta_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not datos_generales.objects.filter(cod_expediente=codi).exists():
					incompletos.append(0)
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-5)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-6)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-7)	
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-9)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
			estado = motivo_consulta.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = MotivoConsultaForm_consultar(instance=estado)
			else: 
				form = MotivoConsultaForm_consultar(request.POST, instance=estado)
				return redirect('/informacion/estado_general/consultar/%s/%s/' %(codi,num))
		return render(request,'informacion/form_motivoconsulta_consultar.html',{'form':form,'num':num,'codi':codi,'completada':ids.completada,'incompletos':incompletos, 'nombreUser':nombreUser})
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})


def Motivo_Consulta_editar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			if ids:
				incompletos =list()
				ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
				for fi in ficha:
					if not datos_generales.objects.filter(cod_expediente=codi).exists():
						incompletos.append(0)
					if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
					if not estado_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-2)
					if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-3)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-4)
					if not registro.objects.filter(fichas_id=fi.id).exists():
							incompletos.append(-5)
							incompletos.append(-6)
							incompletos.append(-7)
					if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-8)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
							incompletos.append(-9)
					if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-10)
					if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-11)
					if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-12)
					if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-13)
					if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-14)
					if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-15)
					if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-16)
					if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-17)
					if not nance_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-18)
					if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-19)
					if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-20)
					if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-21)
				estado = motivo_consulta.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = MotivoConsultaForm(instance=estado)
				else: 
					form = MotivoConsultaForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
						return redirect('/informacion/estado_general/editar/%s/%s/' %(codi,num))
					else:
						return render(request,'informacion/form_motivoconsulta_editar1.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
			return render(request,'informacion/form_motivoconsulta_editar1.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
		except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})


##################################################################################################

def EstadoGeneral_crear(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
						incompletos.append(-2)
						incompletos.append(-3)
			if estado_general.objects.filter(fichas_id=ids.id).exists():
				estado = estado_general.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = EstadoGeneralForm(instance=estado)
				else: 
					form = EstadoGeneralForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
					return redirect('/tipo_perfil/nuevo/%s/%s/' %(codi,num))
				return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi,'ids':ids.id,'incompletos':incompletos, 'nombreUser':nombreUser})

			if request.method == 'POST':
				form = EstadoGeneralForm(request.POST)
				if form.is_valid():
				 	form.save()
				return HttpResponseRedirect('/tipo_perfil/nuevo/%s/%s/' %(codi,num))		
			else:
				if int(num)>1:
					form = EstadoGeneralForm(initial={'fichas':ids.id})	
					fichass = fichas.objects.filter(cod_expediente=codi)
					num_fichas = len(fichass)
					for i in fichass:
						numero = fichas.objects.get(cod_expediente=codi,numero=i.numero)
						if estado_general.objects.filter(fichas_id=numero.id):
							estado = estado_general.objects.get(fichas_id=numero.id)
							form = EstadoGeneralForm(instance=estado)

					return render(request, 'informacion/form_estadoGeneral.html', {'form':form,'codi': codi,'num':num,'ids':ids.id,'incompletos':incompletos, 'nombreUser':nombreUser})
					
				else:
					form = EstadoGeneralForm(initial={'fichas':ids.id})		
					return render(request, 'informacion/form_estadoGeneral.html', {'form':form,'codi': codi,'num':num,'ids':ids.id,'incompletos':incompletos, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_tiene_permiso.html', {'nombreUser':nombreUser})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})



def EstadoGeneral_consultar(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not datos_generales.objects.filter(cod_expediente=codi).exists():
					incompletos.append(0)
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-5)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-6)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-7)	
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-9)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
			estado = estado_general.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = EstadoGeneralForm_consultar(instance=estado)
			else: 
				form = EstadoGeneralForm_consultar(request.POST, instance=estado)
				return redirect('/tipo_perfil/consultar/%s/%s/' %(codi,num))
			return render(request,'informacion/form_estadoGeneral_consultar.html',{'form':form,'num':num,'codi':codi,'completada':ids.completada,'incompletos':incompletos, 'nombreUser':nombreUser})
		return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	



def EstadoGeneral_edit(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			if ids:
				incompletos =list()
				ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
				for fi in ficha:
					if not datos_generales.objects.filter(cod_expediente=codi).exists():
						incompletos.append(0)
					if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
					if not estado_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-2)
					if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-3)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-4)
					if not registro.objects.filter(fichas_id=fi.id).exists():
							incompletos.append(-5)
							incompletos.append(-6)
							incompletos.append(-7)
					if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-8)
					if not registro.objects.filter(fichas_id=fi.id).exists():
						if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
							incompletos.append(-9)
					if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-10)
					if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-11)
					if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-12)
					if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-13)
					if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-14)
					if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-15)
					if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-16)
					if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-17)
					if not nance_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-18)
					if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-19)
					if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-20)
					if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-21)
				estado = estado_general.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = EstadoGeneralForm(instance=estado)
				else: 
					form = EstadoGeneralForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
					return redirect('/tipo_perfil/editar/%s/%s/' %(codi,num))
				return render(request,'informacion/form_estadoGeneral_editar.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
				if int(num)>1:
					return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
				else:
					return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})


def EstadoGeneral_edit2(request,codi,num):
	str(codi)
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			if ids:
				estado = estado_general.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = EstadoGeneralForm(instance=estado)
				else: 
					form = EstadoGeneralForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
					return redirect('/tipo_perfil/nuevo/%s/%s/' %(codi,num))
				return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})

################################################################################################

def eliminar(request):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			return render(request, 'informacion/eliminar.html', {'form':form, 'nombreUser':nombreUser})
	else:
		return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})


class ajax_eliminar(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.rol==1:
			codigo = request.GET['codigo']
			if datos_generales.objects.filter(cod_expediente=codigo).exists():
				datos_generales.objects.filter(cod_expediente=codigo).delete()
				return HttpResponse("Se elimino correctamente")	
		else:
			return HttpResponse('Error la ficha no se pudo eliminar', status=401)

class ajax_eliminar_ficha(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.rol==1:
			codigo = request.GET['codigo']
			numero = request.GET['numero']
			if fichas.objects.filter(cod_expediente=codigo,numero=numero).exists():
				fichas.objects.filter(cod_expediente=codigo,numero=numero).delete()
				return HttpResponse("Se elimino correctamente")
			else:
				return HttpResponse('Error la ficha no se pudo eliminar', status=401)
		else:
			return HttpResponse('Error la ficha no se pudo eliminar', status=401)
################################################################################################



def retiro_voluntario(request):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			return render(request, 'informacion/retiro_voluntario.html', {'form':form, 'nombreUser':nombreUser})	
		else:
			return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})
	else:
		return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})


class ajax_retiro_voluntario(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

		if request.user.rol==1:
			codigo = request.GET['codigo']
			numero = request.GET['numero']
			if  not fichas.objects.filter(cod_expediente_id=codigo,numero=numero,completada=0).exists():
				return HttpResponse('La ficha ya se encuentra Retirada', status=401)
			if fichas.objects.filter(cod_expediente_id=codigo,numero=numero,completada=0).exists():
				fichas.objects.filter(cod_expediente_id=codigo,numero=numero).update(completada=2)
				return HttpResponse("Se retiro correctamente")
		else:
			return render(request, 'base/error_no_tiene_permiso_admin.html')
################################################################################################

def caducada(request):
	nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

	if request.user.rol==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			incompletas = fichas.objects.filter(completada=0)
			num_incompletas = len(incompletas)
			return render(request, 'informacion/caducada.html', {'form':form,'num_incompletas':num_incompletas, 'nombreUser':nombreUser})
	else:
		return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})


class ajax_caducada(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreUser = str(request.user.first_name.encode('utf-8')) + " " + str(request.user.last_name.encode('utf-8'))

		if request.user.rol==1:
			if fichas.objects.filter(completada=0).exists():
				fichas.objects.filter(completada=0).update(completada=3)
				return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})
			else:
				return HttpResponse('No se encuentran fichas incompletas', status=401)
		else:
			return render(request, 'base/error_no_tiene_permiso_admin.html', {'nombreUser':nombreUser})