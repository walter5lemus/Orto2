from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	

from app.aspMandibular.forms import *
from app.aspMandibular.models import aspectos_mandibulares1
from app.informacion.models import fichas, datos_generales

# Create your views here.

def asp_mandibular1(request):
	return render(request, 'asp_mandibular1/asp_mandibular1.html')



def asp_mandibular1_view(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:	
		if request.method == 'POST':
			form = aspMandibularForm(request.POST,initial={'fichas':ids.id})
			if form.is_valid():
				form.save()

			return HttpResponseRedirect('/analisis_radiograficos/otrosAspectos/nuevo/%s/%s/' %(codi,num))
		else: 
			form = aspMandibularForm(initial={'fichas':ids.id})
			
	return render(request,'asp_mandibular1/form_asp_mandibular1.html', {'form':form,'codi':codi,'num':num}) 		   
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")




def asp_mandibular1_edit(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		datos = aspectos_mandibulares1.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = aspMandibularForm(instance=datos)
		else: 
			form = aspMandibularForm(request.POST, instance=datos)
			if form.is_valid():
				form.save()
			return redirect('/denticion/sagitales/editar/%s/%s' %(codi,num))
		return render(request, 'asp_mandibular1/form_asp_mandibular1.html',{'form':form})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	#except Exception, e:
	#	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def asp_mandibular1_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			datos = aspectos_mandibulares1.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = aspMandibularForm_consultar(instance=datos)
			else: 
				form = aspMandibularForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return redirect('/denticion/sagitales/consultar/%s/%s' %(codi,num))
			return render(request, 'asp_mandibular1/form_asp_mandibular1.html',{'form':form})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


	