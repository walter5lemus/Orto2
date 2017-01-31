from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	

from app.diagCefalo.forms import *
from app.diagCefalo.models import diagnostico_cefalometrico
from app.informacion.models import fichas, datos_generales


# Create your views here.

def diag_cefalo(request):
	return render(request, 'diag_cefalo/diag_cefalo.html')


def diag_cefalo_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:	
			if request.method == 'POST':
				form = diagCefaloForm(request.POST,initial={'fichas':ids.id})
				if form.is_valid():
					form.save()

				return HttpResponseRedirect('/analisis_radiograficos/analisis_nance/nuevo/%s/%s/' %(codi,num))
			else: 
				form = diagCefaloForm(initial={'fichas':ids.id})
				
		return render(request,'diag_cefalo/form_diag_cefalo.html', {'form':form,'codi':codi,'num':num})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")



def diag_cefalo_edit(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		datos = diagnostico_cefalometrico.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = diagCefaloForm(instance=datos)
		else: 
			form = diagCefaloForm(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return redirect('/denticion/sagitales/editar/%s/%s' %(codi,num))
		return render(request, 'diag_cefalo/form_diag_cefalo.html',{'form':form,'num':num,'codi':codi})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")



def diag_cefalo_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			datos = diagnostico_cefalometrico.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = diagCefaloForm_consultar(instance=datos)
			else: 
				form = diagCefaloForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return redirect('/denticion/sagitales/consultar/%s/%s' %(codi,num))
			return render(request, 'diag_cefalo/form_diag_cefalo.html',{'form':form,'num':num,'codi':codi})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

