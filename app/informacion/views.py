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

codi=""

class CodExpediente_List(ListView):
	model = codigo_expediente
	template_name = 'informacion/list_cod_expediente.html'

def CodExpediente_crear(request):

	if request.method == 'POST':
		form = DatosGeneralesForm(request.POST)
		codi = form.data['codigo'] 
		#num = form.data['num']
		if form.is_valid():
		 	form.save()
	else:
		form = DatosGeneralesForm()
		return render(request, 'informacion/form_inicio.html', {'form':form})

class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		nombre = request.GET['nombre']
		cod = datos_generales.objects.get(nombre_completo=nombre)
		datosGenerales = datos_generales.objects.filter(cod_expediente=cod)
		if codigo_expediente.objects.filter(codigo=cod).exists():{
		}
		else:
			codigo_expediente.objects.create(codigo=cod)
		data = serializers.serialize('json', datosGenerales, fields=('nombre_completo','fechaRegistro','fecha_hora_creacion','cod_expediente'))
		return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		nombre = request.GET['nombre']
		cod = datos_generales.objects.get(nombre_completo=nombre)
		fi=list(fichas.objects.filter(cod_expediente=cod.cod_expediente))
		for ficha in fi:
			ids= fichas.objects.get(cod_expediente_id=ficha.cod_expediente_id,numero=ficha.numero)

			if estado_general.objects.filter(fichas_id=ids.id).exists():{}
			else:
				fichas.objects.get(id=ids.id).delete()
		fi=list(fichas.objects.filter(cod_expediente=cod))
		data = serializers.serialize('json', fi, fields=('numero'))
		return HttpResponse(data, content_type='application/json')

def busqueda(request):
	if request.is_ajax():
		resultado = datos_generales.objects.filter(nombre_completo__startswith= request.GET['nombre'] ).values('nombre_completo', 'cod_expediente')
		return HttpResponse( json.dumps( list(resultado)), content_type='application/json')

class busquedaCodigo(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		cod = datos_generales.objects.filter(cod_expediente=codigo)
		if fichas.objects.filter(cod_expediente=codigo).exists():{}
		else:
			datos_generales.objects.filter(cod_expediente=codigo).delete()
			codigo_expediente.objects.filter(codigo=codigo_expediente).delete()
		data = serializers.serialize('json', cod, fields=('cod_expediente'))
		return HttpResponse(data, content_type='application/json')

def CodExpediente_consular(request):

	if request.method == 'POST':
		form = CodigoExpedienteForm(request.POST)
		codi = form.data['codigo']
		if form.is_valid():
		 	form.save()
 			return HttpResponseRedirect('/informacion/estado_general/consultar/%s/' %codi)
	 	else:
 			return HttpResponseRedirect('/informacion/estado_general/consultar/%s/' %codi)

	else:
			form = CodigoExpedienteForm()

			return render(request, 'informacion/form_inicio_consultar.html', {'form':form})

def CodExpediente_editar(request):

	if request.method == 'POST':
		form = CodigoExpedienteForm(request.POST)
		codi = form.data['codigo'] 
		if form.is_valid():
		 	form.save()
 			return HttpResponseRedirect('/informacion/estado_general/editar/%s/' %codi)
	 	else:
 			return HttpResponseRedirect('/informacion/estado_general/editar/%s/' %codi)

	else:
			form = CodigoExpedienteForm()

			return render(request, 'informacion/form_inicio_editar.html', {'form':form})

###############################################################################
class DatosGeneralesList(ListView):
	model = datos_generales
	template_name = 'informacion/list_datosgenerales.html'

def DatosGeneral_crear(request):
	user = request.user.id
	num = 1

	if request.method == 'POST':
			form = DatosGeneralesForm(request.POST)
			codi = request.POST.get('cod_expediente')
			if form.is_valid():
				
			 	form.save()
			return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/%s' %(codi,num)) 
	else:
			form = DatosGeneralesForm(initial={'usuario_creador':request.user.id})
			
				
	return render(request, 'informacion/form_datosGenerales.html', {'form':form,'num':num})

def DatosGenerales_consultar(request,codi):
	str(codi)
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
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %codi)
			return render(request,'informacion/form_datosGenerales.html',{'form':form})
		return HttpResponse("No se encontro el Codigo de Expediente")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")

def DatosGenerales_consultar2(request,codi):
	#str(codi)
	#try:
	ids = datos_generales.objects.get(cod_expediente=codi)
	if ids:
		datos = datos_generales.objects.get(cod_expediente=codi)
		if request.method == 'GET':
			form = DatosGeneralesForm_consultar(instance=datos)
		else: 
			form = DatosGeneralesForm_consultar(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/' %codi)
		return render(request,'informacion/form_datosGenerales_existente.html',{'form':form,'codi':codi,'num':num})
	return HttpResponse("No se encontro el Codigo de Expediente")
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente")

def DatosGenerales_edit(request,codi):
	str(codi)
	try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm(instance=datos)
			else: 
				form = DatosGeneralesForm(request.POST, instance=datos)
				if form.is_valid():
					co = request.POST.get('cod_expediente')
					form.save()
				#return redirect('informacion:datos_generales_listar')
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %co)
			return render(request,'informacion/form_datosGenerales.html',{'form':form,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")

################################################################################################

def Motivo_Consulta_crear(request,codi,num):
	
	if fichas.objects.filter(cod_expediente_id=codi, numero=num).exists():{}
	else:
		fichas.objects.create(cod_expediente_id=codi, numero=num, usuario_creador_id=request.user.id)
		if not codigo_expediente.objects.filter(codigo=codi).exists():
			codigo_expediente.objects.create(codigo=codi)

	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	
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
				print "fecha 2"
				print fecha
				ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
				return redirect('/informacion/estado_general/nuevo/%s/%s/' %(codi,num))
			return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	else:
		fecha =  timezone.now()
		print fecha

		if ultima_modificacion.objects.filter(fichas_id=ids.id).exists():{}
		else:
			ultima_modificacion.objects.create(fichas_id=ids.id,fecha=fecha)

		if request.method == 'POST':
			
			form = MotivoConsultaForm(request.POST)
			if form.is_valid():
			 	form.save()

			return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/%s' %(codi,num))
		else:
			
			form = MotivoConsultaForm(initial={'fichas':ids.id,'fecha_hora_creacion':fecha})
			
			return render(request, 'informacion/form_motivoconsulta.html', {'form':form,'codi': codi,'num':num})

	
def Motivo_Consulta_editar2(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = motivo_consulta.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = MotivoConsultaForm(instance=estado)
			else: 
				form = MotivoConsultaForm(request.POST, instance=estado)
				if form.is_valid():
					form.save()
				return redirect('/informacion/estado_general/editar/%s/%s/' %(codi,num))
			return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def Motivo_Consulta_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = motivo_consulta.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = MotivoConsultaForm_consultar(instance=estado)
			else: 
				form = MotivoConsultaForm_consultar(request.POST, instance=estado)

				return redirect('/informacion/estado_general/consultar/%s/%s/' %(codi,num))
			return render(request,'informacion/form_motivoconsulta_consultar.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def Motivo_Consulta_editar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = motivo_consulta.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = MotivoConsultaForm(instance=estado)
			else: 
				form = MotivoConsultaForm(request.POST, instance=estado)
				if form.is_valid():
					form.save()
				return redirect('/informacion/estado_general/nuevo/%s/%s/' %(codi,num))
			return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

	

##################################################################################################

class EstadoGeneralList(ListView):
	model = estado_general
	template_name = 'informacion/list_estadogeneral.html'

def EstadoGeneral_crear(request,codi,num):
	str(codi)
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
		return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi})

	if request.method == 'POST':
		form = EstadoGeneralForm(request.POST)
		if form.is_valid():
		 	form.save()
		return HttpResponseRedirect('/tipo_perfil/nuevo/%s/%s/' %(codi,num))		
	else:		
		#if fichas.objects.filter(cod_expediente_id=codi, numero=num).exists():{}
		#else:{
			#fichas.objects.create(cod_expediente_id=codi, numero=num, usuario_creador_id=request.user.id)
		#}
		form = EstadoGeneralForm(initial={'fichas':ids.id})
		
		return render(request, 'informacion/form_estadoGeneral.html', {'form':form,'codi': codi,'num':num})	

def EstadoGeneral_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = estado_general.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = EstadoGeneralForm_consultar(instance=estado)
			else: 
				form = EstadoGeneralForm_consultar(request.POST, instance=estado)

				return redirect('/tipo_perfil/consultar/%s/%s/' %(codi,num))
			return render(request,'informacion/form_estadoGeneral_consultar.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")



def EstadoGeneral_edit(request,codi,num):
	str(codi)
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
				return redirect('/tipo_perfil/edit/%s/%s/' %(codi,num))
			return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def EstadoGeneral_edit2(request,codi,num):
	str(codi)
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
			return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")



################################################################################################


