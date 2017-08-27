from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect	
from app.informacion.models import *

from app.aspMandibular.forms import *
from app.analisis_cefalometrico.models import *
from app.analisis_radiograficos.models import *
from app.AnalisisDenticionMixta.models import *
from app.aspMandibular.models import *
from app.aspectos.models import *
from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.informacion.models import *
from app.tipo_perfil.models import *

# Create your views here.

def asp_mandibular1(request):
	return render(request, 'asp_mandibular1/asp_mandibular1.html')



def asp_mandibular1_view(request,codi,num):
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
				return render(request, 'asp_mandibular1/form_asp_mandibular1.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
			else:
				if ids:	
					if request.method == 'POST':
						form = aspMandibularForm(request.POST,initial={'fichas':ids.id})
						if form.is_valid():
							form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
							return HttpResponseRedirect('/analisis_radiograficos/otrosAspectos/nuevo/%s/%s/' %(codi,num))
						return render(request,'asp_mandibular1/form_asp_mandibular1.html', {'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser}) 
					else: 
						form = aspMandibularForm(initial={'fichas':ids.id})
						
				return render(request,'asp_mandibular1/form_asp_mandibular1.html', {'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser}) 
		else:
			return render(request, 'base/error_no_tiene_permiso.html', {'nombreUser':nombreUser})
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
		else:
			return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	




def asp_mandibular1_edit(request,codi,num):
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
				return render(request, 'asp_mandibular1/form_asp_mandibular1_editar.html',{'form':form,'codi':codi,'num':num,'incompletos':incompletos, 'nombreUser':nombreUser})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1, 'nombreUser':nombreUser})
			else:
				return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})	
	else:
		return render(request, 'base/error_no_hay_acceso.html', {'nombreUser':nombreUser})



def asp_mandibular1_consultar(request,codi,num):
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
			return render(request, 'asp_mandibular1/form_asp_mandibular1_consultar.html',{'form':form,'codi':codi,'num':num,'completada':ids.completada,'incompletos':incompletos, 'nombreUser':nombreUser})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})



	