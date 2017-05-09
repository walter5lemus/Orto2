from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	
from app.informacion.models import *

from app.aspMandibular.forms import *
from app.aspMandibular.models import aspectos_mandibulares1

# Create your views here.

def asp_mandibular1(request):
	return render(request, 'asp_mandibular1/asp_mandibular1.html')



def asp_mandibular1_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			if aspectos_mandibulares1.objects.filter(fichas_id=ids.id).exists():
				datos = aspectos_mandibulares1.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = aspMandibularForm(instance=datos)
				else: 
					form = aspMandibularForm(request.POST, instance=datos)
					if form.is_valid():
						form.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/analisis_radiograficos/otrosAspectos/nuevo/%s/%s' %(codi,num))
				return render(request, 'asp_mandibular1/form_asp_mandibular1.html',{'form':form,'codi':codi,'num':num})
			else:
				if ids:	
					if request.method == 'POST':
						form = aspMandibularForm(request.POST,initial={'fichas':ids.id})
						if form.is_valid():
							form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
							return HttpResponseRedirect('/analisis_radiograficos/otrosAspectos/nuevo/%s/%s/' %(codi,num))
						return render(request,'asp_mandibular1/form_asp_mandibular1.html', {'form':form,'codi':codi,'num':num}) 
					else: 
						form = aspMandibularForm(initial={'fichas':ids.id})
						
				return render(request,'asp_mandibular1/form_asp_mandibular1.html', {'form':form,'codi':codi,'num':num}) 
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	




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
				fecha =  timezone.now()
				ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
				return redirect('/analisis_radiograficos/otrosAspectos/editar/%s/%s' %(codi,num))
		return render(request, 'asp_mandibular1/form_asp_mandibular1.html',{'form':form,'codi':codi,'num':num})
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
					fecha =  timezone.now()
					ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
				return redirect('/analisis_radiograficos/otrosAspectos/consultar/%s/%s' %(codi,num))
			return render(request, 'asp_mandibular1/form_asp_mandibular1_consultar.html',{'form':form,'codi':codi,'num':num,'completada':ids.completada})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')



	