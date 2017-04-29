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

def CodExpediente_crear(request):

	if request.method == 'POST':
		form = DatosGeneralesForm(request.POST)
		codi = form.data['codigo'] 
		if form.is_valid():
		 	form.save()
	else:
		form = DatosGeneralesForm()
		return render(request, 'informacion/form_inicio.html', {'form':form})

class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		cod = list(datos_generales.objects.filter(cod_expediente=codigo))
		data = serializers.serialize('json', cod)
		return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		fi=fichas.objects.filter(cod_expediente=codigo)
		for ficha in fi:
			ids= fichas.objects.get(cod_expediente_id=ficha.cod_expediente_id,numero=ficha.numero)
			if motivo_consulta.objects.filter(fichas_id=ids.id).exists():{}
			else:
				fichas.objects.get(id=ids.id).delete()
		fi=list(fichas.objects.filter(cod_expediente=codigo))
		data = serializers.serialize('json', fi, fields=('numero'))
		return HttpResponse(data, content_type='application/json')

def busqueda(request):
	if request.is_ajax():
		resultado = datos_generales.objects.filter(nombre_completo__istartswith= request.GET['nombre'] ).values('nombre_completo', 'cod_expediente')
		return HttpResponse( json.dumps( list(resultado)), content_type='application/json')

def busqueda_admin(request):
	if request.user.id==1:
		if request.is_ajax():
			resultado = datos_generales.objects.filter(nombre_completo__istartswith= request.GET['nombre'] ).values('nombre_completo', 'cod_expediente')
			return HttpResponse( json.dumps( list(resultado)), content_type='application/json')

def busqueda2_admin(request):
	if request.user.id==1:
		if request.is_ajax():
			resultado = fichas.objects.filter(cod_expediente_id__cod_expediente__startswith=request.GET['codigo']).values('cod_expediente')
			return HttpResponse( json.dumps( list(resultado)), content_type='application/json')

class busquedaCodigo(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['codigo']
		if fichas.objects.filter(cod_expediente=codigo).exists():
			cod = datos_generales.objects.filter(cod_expediente=codigo)
			data = serializers.serialize('json', cod, fields=('cod_expediente'))
			return HttpResponse(data, content_type='application/json')
		return HttpResponse("")

class busqueda_codigo(TemplateView):
	def get(self,request,*args,**kwargs):
		codigo = request.GET['cod_expediente']
		if fichas.objects.filter(cod_expediente=codigo).exists():
			cod = datos_generales.objects.filter(cod_expediente=codigo)
			data = serializers.serialize('json', cod, fields=('cod_expediente'))
			return HttpResponse(data, content_type='application/json')
		return HttpResponse("")	

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
			form = DatosGeneralesForm()
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
				return render(request, 'informacion/form_datosGenerales.html', {'form':form,'num':num})
	else:
			form = DatosGeneralesForm(initial={'usuario_creador':request.user.id})
	return render(request, 'informacion/form_datosGenerales.html', {'form':form,'num':num})

def DatosGeneral_crear2(request,codi,num):
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
					form.save()
					return HttpResponseRedirect('/informacion/motivo_consultas/nuevo/%s/%s' %(codi,num))
				else:
					return render(request,'informacion/form_datosGenerales2.html',{'form':form,'codi':codi,'num':num})
			return render(request,'informacion/form_datosGenerales2.html',{'form':form,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")


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
				return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/' %codi)
			return render(request,'informacion/form_datosGenerales_existente.html',{'form':form,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

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
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %co)
			return render(request,'informacion/form_datosGenerales.html',{'form':form,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")

################################################################################################

def Motivo_Consulta_crear(request,codi,num):
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
		ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)
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
						return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi})
				return render(request,'informacion/form_motivoconsulta.html',{'form':form,'num':num,'codi':codi})
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
					return render(request, 'informacion/form_motivoconsulta.html', {'form':form,'codi': codi,'num':num})
			else:
				form = MotivoConsultaForm(initial={'fichas':ids.id,'fecha_hora_creacion':fecha})
				return render(request, 'informacion/form_motivoconsulta.html', {'form':form,'codi': codi,'num':num})
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	
	
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
			return render(request,'informacion/form_motivoconsulta_consultar.html',{'form':form,'num':num,'codi':codi,'completada':ids.completada})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

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
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)
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
			form = EstadoGeneralForm(initial={'fichas':ids.id})
			
			return render(request, 'informacion/form_estadoGeneral.html', {'form':form,'codi': codi,'num':num})	
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')

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
		return render(request, 'base/error_no_encontrado.html')	
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')	

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

def eliminar(request):
	if request.user.is_superuser==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			return render(request, 'informacion/eliminar.html', {'form':form})
	else:
		return render(request, 'base/error_no_hay_acceso.html')


class ajax_eliminar(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.is_superuser==1:
			codigo = request.GET['codigo']
			if datos_generales.objects.filter(cod_expediente=codigo).exists():
				datos_generales.objects.filter(cod_expediente=codigo).delete()
				return HttpResponse("Se elimino correctamente")	
		else:
			return HttpResponse('Error la ficha no se pudo eliminar', status=401)

class ajax_eliminar_ficha(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.is_superuser==1:
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
	if request.user.is_superuser==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			return render(request, 'informacion/retiro_voluntario.html', {'form':form})	
		else:
			return render(request, 'base/error_no_hay_acceso.html')
	else:
		return render(request, 'base/error_no_hay_acceso.html')

class ajax_retiro_voluntario(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.is_superuser==1:
			codigo = request.GET['codigo']
			numero = request.GET['numero']
			if  not fichas.objects.filter(cod_expediente_id=codigo,numero=numero,completada=0).exists():
				return HttpResponse('La ficha ya se encuentra Retirada', status=401)
			if fichas.objects.filter(cod_expediente_id=codigo,numero=numero,completada=0).exists():
				fichas.objects.filter(cod_expediente_id=codigo,numero=numero).update(completada=2)
				return HttpResponse("Se retiro correctamente")
		else:
			return render(request, 'base/error_no_hay_acceso.html')
################################################################################################

def caducada(request):
	if request.user.is_superuser==1:
		if request.method == 'GET':
			form = DatosGeneralesForm()
			return render(request, 'informacion/caducada.html', {'form':form})
	else:
		return render(request, 'base/error_no_hay_acceso.html')
class ajax_caducada(TemplateView):
	def get(self,request,*args,**kwargs):
		if request.user.is_superuser==1:
			if fichas.objects.filter(completada=0).exists():
				fi = fichas.objects.filter(completada=0)
				for ficha in fi:
					print ficha
				fichas.objects.filter(completada=0).update(completada=3)
				return HttpResponse("Se retiro correctamente")
			else:
				return HttpResponse('No se encuentran fichas incompletas', status=401)
		else:
			return render(request, 'base/error_no_hay_acceso.html')
