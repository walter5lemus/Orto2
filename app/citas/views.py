from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect	
import json
from django.core import serializers
from app.citas.forms import *
from app.citas.models import *
from app.informacion.models import *

# Create your views here.
def citas_crear(request):
	
	user = request.user.id
	if request.method == 'POST':
		form2 = citasForm(request.POST,initial={})
		form = citasGeneralesForm(request.POST,initial={})
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return HttpResponseRedirect('/')
	else:

		form2 = citasForm(initial={})
		form = citasGeneralesForm(initial={'estudiante':request.user.username})
	return render(request, 'citas/citas_crear.html', {'form':form,'form2':form2})

def citas_crear2(request):
	
	user = request.user.id
	if request.method == 'POST':
		form2 = citasForm(request.POST,initial={})
		form = citasGeneralesForm(request.POST,initial={})
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return HttpResponseRedirect('/')
	else:

		form2 = citasForm(initial={})
		form = citasGeneralesForm(initial={'estudiante':request.user.username})
	return render(request, 'citas/citas_crear2.html', {'form':form,'form2':form2})



class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		nombre = datos_generales.objects.filter(cod_expediente=cod)
		citass = citas_general.objects.filter(codigo_id=cod)
		
		data = serializers.serialize('json', nombre, fields=('nombre_completo'))

		return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		#nombre = datos_generales.objects.filter(cod_expediente=cod)
		citass = citas_general.objects.filter(codigo_id=cod)
		#algo = citass[0]
		#aparato2 = dict(aparato_choices).get(algo['aparato'])
		data = serializers.serialize('json', citass, fields=('aparato'))
		#data = json.dumps({
        #'aparato': aparato2,
    	#})
		return HttpResponse(data, content_type='application/json')


class BusquedaCitasListar(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		citas2 = citas.objects.filter(codigo_id=cod)

		data2 = serializers.serialize('json', citas2,fields=('codigo','num_cita','fecha_cita','observaciones','proxima_cita','resultados','autorizacion','tutor'))
		return HttpResponse(data2, content_type='application/json')



def registrocita(request,codi):
	user = request.user.id
	str(codi)
	entro = 0;
	
	num=0 
	queryset = citas_general.objects.filter(codigo_id=codi)
	if queryset:
		entro = 1
		num = len(queryset)
	#	return HttpResponseRedirect('/informacion/datos_generales/editar/%s/' %codi)
	
	if request.method == 'POST':
		if entro == 1:
			form2 = citasForm2(request.POST)
			if form2.is_valid():
				form2.save()
			return HttpResponseRedirect('/citas/cerrar/')
		else:
			
			form2 = citasForm2(request.POST)
			form = citasGeneralesForm2(request.POST)
			if form.is_valid() and form2.is_valid():
				form.save()
				form2.save()
			return HttpResponseRedirect('/citas/cerrar/')
	else:

		if entro ==	 1:
			form2 = citasForm2(initial={'codigo':codi,'num_cita':num+1})
			return render(request, 'citas/ventana2.html', {'form2':form2})	
		else:
			form = citasGeneralesForm2(initial={'codigo':codi,'estudiante':request.user.id})
			form2 = citasForm2(initial={'codigo':codi,'num_cita':num+1})
			
			return render(request, 'citas/ventana1.html', {'form':form,'form2':form2})
