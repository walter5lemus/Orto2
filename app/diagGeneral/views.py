from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	

from app.diagGeneral.forms import *
from app.diagGeneral.models import diagnostico_general
from app.informacion.models import fichas, datos_generales


# Create your views here.

def diag_general(request):
	return render(request, 'diag_general/diag_general.html')


def diag_general_view(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)

	if diagnostico_general.objects.filter(fichas_id=ids.id).exists():
		datos = diagnostico_general.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = diagGeneralForm(instance=datos)
		else: 
			form = diagGeneralForm(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return redirect('/')
		return render(request, 'diag_general/form_diag_general.html',{'form':form,'num':num,'codi':codi})

	else:
		if ids:	
			if request.method == 'POST':
				form = diagGeneralForm(request.POST,initial={'fichas':ids.id})
				if form.is_valid():
					form.save()

				return HttpResponseRedirect('/')
			else: 
				form = diagGeneralForm(initial={'fichas':ids.id})
		
	return render(request,'diag_general/form_diag_general.html', {'form':form,'codi':codi,'num':num})
#	except Exception, e:
#		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")



def diag_general_edit(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		datos = diagnostico_general.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = diagGeneralForm(instance=datos)
		else: 
			form = diagGeneralForm(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return redirect('/')
		return render(request, 'diag_general/form_diag_general.html',{'form':form,'num':num,'codi':codi})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def diag_general_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			datos = diagnostico_general.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = diagGeneralForm_consultar(instance=datos)
			else: 
				form = diagGeneralForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return redirect('/')
			return render(request, 'diag_general/form_diag_general_consultar.html',{'form':form,'num':num,'codi':codi})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


	

	