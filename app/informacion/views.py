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

codi=""

class CodExpediente_List(ListView):
	model = codigo_expediente
	template_name = 'informacion/list_cod_expediente.html'

def CodExpediente_crear(request):

	if request.method == 'POST':
		form = DatosGeneralesForm(request.POST)
		codi = form.data['codigo'] 
		if form.is_valid():
		 	form.save()
 			return HttpResponseRedirect('/informacion/datos_generales/nuevo/%s/' %codi)
	 	else:
	 		try:
	 			existe = datos_generales.objects.get(cod_expediente = codi)
		 		if existe:
		 			return HttpResponseRedirect('/informacion/datos_generales/consultar2/%s/' %codi)
		 		else:
		 			return HttpResponseRedirect('/informacion/datos_generales/nuevo/%s/' %codi)
	 		except Exception, e:
				return HttpResponseRedirect('/informacion/datos_generales/nuevo/%s/' %codi)

	else:
			form = DatosGeneralesForm()

			return render(request, 'informacion/form_inicio.html', {'form':form,'codi':codi,'num':num})

class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		datosGenerales = datos_generales.objects.filter(cod_expediente=cod)
		data = serializers.serialize('json', datosGenerales, fields=('nombre_completo','fechaRegistro','fecha_hora_creacion'))
		return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		fi=list(fichas.objects.filter(cod_expediente=cod))
		for ficha in fi:
			ids= fichas.objects.get(cod_expediente_id=ficha.cod_expediente_id,numero=ficha.numero)

			if estado_general.objects.filter(fichas_id=ids.id).exists():{}
			else:
				fichas.objects.get(id=ids.id).delete();
		fi=list(fichas.objects.filter(cod_expediente=cod))
		data = serializers.serialize('json', fi, fields=('numero'))
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

def DatosGeneral_crear(request,codi):
	str(codi)
	user = request.user.id
	num = 1
	if datos_generales.objects.filter(cod_expediente=codi).exists():
		return HttpResponseRedirect('/informacion/datos_generales/editar/%s/' %codi)
	
	if request.method == 'POST':
			form = DatosGeneralesForm(request.POST)
			if form.is_valid():
			 	form.save()
			return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/%s' %(codi,num)) 
	else:
			form = DatosGeneralesForm(initial={'cod_expediente':codi,'usuario_creador':request.user.id})

	return render(request, 'informacion/form_datosGenerales.html', {'form':form,'codi':codi,'num':num})

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
			return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %codi)
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




##################################################################################################


class FichasList(ListView):
	model = fichas
	template_name = 'informacion/list_fichas.html'


num=1
def Fichas_crear(request,codi):
	str(codi)
	ids = datos_generales.objects.get(cod_expediente=codi)


	d=OrderedDict()
 	fi=list(fichas.objects.filter(cod_expediente=codi))
 	if fi:
	 	ultimo = fi[-1]
	 	numer=ultimo.numero+1
	else:
	 	numer=1

	if fichas.objects.filter(cod_expediente_id=codi, numero=numer-1).exists():
		try:
			d = fichas.objects.get(cod_expediente_id=codi, numero=numer-1)
			if estado_general.objects.filter(fichas_id=d.id).exists():{}
			else:
				fichas.objects.get(cod_expediente_id=codi, numero=numer-1).delete();
				numer-1;
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %codi)
		except Exception as e:
			raise e
		 


	if ids:
		if request.method == 'POST':
				form = FichasForm(request.POST)
				if form.is_valid():
					global num
					num = request.POST.get('numero')
				
				return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/%s/' %(codi,num))
		else:

			form = FichasForm(initial={'cod_expediente':codi,'numero':numer})

	return render(request, 'informacion/form_fichas.html', {'form':form, 'numer':numer})



##################################################################################################
class EstadoGeneralList(ListView):
	model = estado_general
	template_name = 'informacion/list_estadogeneral.html'

def EstadoGeneral_crear(request,codi,num):
	str(codi)


	if request.method == 'POST':
		form = EstadoGeneralForm(request.POST)
		if form.is_valid():
		 	form.save()

		return HttpResponseRedirect('/tipo_perfil/nuevo/%s/%s/' %(codi,num))
		
	else:

		
		if fichas.objects.filter(cod_expediente_id=codi, numero=num).exists():{}
		else:{
			fichas.objects.create(cod_expediente_id=codi, numero=num)
		}
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
			return render(request,'informacion/form_estadoGeneral.html',{'form':form,'num':num,'codi':codi})
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


