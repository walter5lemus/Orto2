	# -*- coding: utf-8 -*-
from django import forms
from app.informacion.models import *
from django.contrib.admin import widgets
from app.informacion.choices import *
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 

class UserForm(UserCreationForm):
	class Meta:
		model = Usuario

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'dui',
			'carnet',
		]
		labels = {
			'username': 'Nombre de Usuario',
			'first_name':'Nombres',
			'last_name': 'Apellidos',
			'email':'Correo',
			'dui':'Dui',
			'carnet':'Carnet',
		}

class DatosGeneralesForm(forms.ModelForm):
	class Meta:
		model = datos_generales
		this_year = datetime.now().year+1

		fields = [
			'cod_expediente',
			'nombre_completo',
			'edad',
			'edad_registro',
			'fecha_nac',
			'telefono',
			'genero',
			'direccion',
			'departamento',
			'nombre_resp',
			'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Código Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Teléfono',
			'genero':'Genero',
			'direccion':'Dirección',
			'departamento':'Departamento',
			'nombre_resp':'Nombre del Padre o Encargado',
			'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creación',
		}

		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control', 'pattern':'[0-9]{4}[-]{1}[0-9]{2}','title':'Ejemplo: 0001-16','autocomplete':'off'}),
			'nombre_completo':forms.TextInput(attrs={'class':'form-control','title':'El nombre no puede incluir numeros o caracteres especiales','pattern':'[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ]{2,100}'}),
			'edad':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'edad_registro':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'fecha_nac':forms.SelectDateWidget(years=range(1950,this_year,1),attrs={'class':'form-control fecha','style': 'width: 243px; display: inline-block;'}),
			'telefono':forms.TextInput(attrs={'class':'form-control', 'pattern':'[0-9]{8}','title':'Ejemplo: 77777777'}),
			'genero':forms.Select(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'departamento':forms.Select(attrs={'class':'form-control'}),
			'nombre_resp':forms.TextInput(attrs={'class':'form-control','pattern':'[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.-]{2,100}'}),
			'usuario_creador':forms.HiddenInput(attrs={'class':'form-control'}),
			'fecha_hora_creacion':forms.DateTimeInput(attrs={'class':'form-control','readonly':'true'}),
		
		}



class DatosGeneralesForm_consultar(forms.ModelForm):
	class Meta:
		model = datos_generales

		fields = [
			'cod_expediente',
			'nombre_completo',
			'edad',
			'edad_registro',
			'fecha_nac',
			'telefono',
			'genero',
			'direccion',
			'departamento',
			'nombre_resp',
			'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Código Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Teléfono',
			'genero':'Genero',
			'direccion':'Dirección',
			'departamento':'Departamento',
			'nombre_resp':'Nombre del Padre o Encargado',
			'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creación',
		}

		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'nombre_completo':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'edad':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'edad_registro':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'fecha_nac':forms.DateInput(attrs={'class':'form-control fecha','readonly':True}),
			'telefono':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'genero':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'direccion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'departamento':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'nombre_resp':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'usuario_creador':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'fecha_hora_creacion':forms.DateTimeInput(attrs={'class':'form-control','readonly':True}),
		
		}


class FichasForm(forms.ModelForm):
	class Meta:
		model = fichas

		fields=[
			'cod_expediente',
			'numero',
		]

		labels={
			'cod_expediente': 'Código de Expediente',
			'numero':'Numero de ficha a crear',
		}
		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'numero':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
		}


class MotivoConsultaForm(forms.ModelForm):
	class Meta:
		model = motivo_consulta
		this_year = datetime.now().year+1
		this_month = datetime.now().month
		this_day = datetime.now().day
		fields = [
			'fichas',
			'motivo_consulta',
			'fechaRegistro',
			'curso',
			'rotacion',
			'turno',
		]
		labels={
			'fichas': 'Código Expediente y Numero de Ficha'	,
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			'curso':'Curso',
			'rotacion':'Rotacion',
			'turno':'Turno',
		}
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control'}),
			'fechaRegistro':forms.SelectDateWidget(years=range(this_year-1,this_year-3,-1),attrs={'class':'form-control','style': 'width: 32.5%; display: inline-block;'}),
			'curso':forms.Select(attrs={'class':'form-control'}),
			'rotacion':forms.Select(attrs={'class':'form-control'}),
			'turno':forms.Select(attrs={'class':'form-control'}),
		}

	def clean(self):

		# Sobrecargar clean devuelve un diccionario con los campos
		cleaned_data = super(MotivoConsultaForm, self).clean()
		valor_propiedad = cleaned_data.get("fechaRegistro")
     
		if valor_propiedad > date.today():
			raise forms.ValidationError({'fechaRegistro': ["La fecha que seleccionó es mayor al dia de ahora",]})
        # Siempre hay que devolver el diccionario
		return cleaned_data
		
class MotivoConsultaForm_consultar(forms.ModelForm):
	class Meta:
		model = motivo_consulta
		this_year = datetime.now().year+1

		fields = [
			'fichas',
			'motivo_consulta',
			'fechaRegistro',
			'curso',
			'rotacion',
			'turno',
		]
		labels={
			'fichas': 'Código Expediente y Numero de Ficha'	,
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			'curso':'Curso',
			'rotacion':'Rotación',
			'turno':'Turno',
		}
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'fechaRegistro':forms.SelectDateWidget(years=range(this_year-1,this_year-3,-1),attrs={'class':'form-control','style': 'width: 32.5%; display: inline-block;','readonly':True}),
			'curso':forms.Select(attrs={'class':'form-control','readonly':True}),
			'rotacion':forms.Select(attrs={'class':'form-control','readonly':True}),
			'turno':forms.Select(attrs={'class':'form-control','readonly':True}),
		}
		



class EstadoGeneralForm(forms.ModelForm):
	class Meta:
		model = estado_general

		fields = [
			'fichas',
			'cambio_salud',
			'detalle_enf_operacion',
			'detalle_medicamento',
			'detalle_otra_enfermedad',
			'otras_enfermedades',
		]

		labels ={
			'fichas': 'Código Expediente y Numero de Ficha'	,
			'cambio_salud' : '¿Ha habido cambio en su salud en el último año?  ',
			'detalle_enf_operacion' : '¿En que consistió la enfermedad u operación?',
			'detalle_medicamento' : '¿Toma algún medicamento?',
			'detalle_otra_enfermedad' : '¿Otras enfermedades?',
			'otras_enfermedades': 'Padeció alguna vez las siguientes enfermedades:',
		}
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'cambio_salud':forms.RadioSelect(attrs={'class':'lista'}),
			'detalle_enf_operacion':forms.Textarea(attrs={'class':'form-control'}),
			'detalle_medicamento':forms.TextInput(attrs={'class':'form-control'}),
			'detalle_otra_enfermedad':forms.TextInput(attrs={'class':'form-control'}),
			'otras_enfermedades': forms.CheckboxSelectMultiple(attrs={'class':'lista'}),
		}


class EstadoGeneralForm_consultar(forms.ModelForm):
	class Meta:
		model = estado_general

		fields = [
			'fichas',
			'cambio_salud',
			'detalle_enf_operacion',
			'detalle_medicamento',
			'detalle_otra_enfermedad',
			'otras_enfermedades',
		]

		labels ={
			'fichas': 'Código Expediente y Numero de Ficha'	,
			'cambio_salud' : '¿Ha habido cambio en su salud en el último año?  ',
			'detalle_enf_operacion' : '¿En que consistió la enfermedad u operación?',
			'detalle_medicamento' : '¿Toma algún medicamento?',
			'detalle_otra_enfermedad' : '¿Otras enfermedades?',
			'otras_enfermedades': 'Padeció alguna vez las siguientes enfermedades:',
		}	
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'cambio_salud':forms.RadioSelect(attrs={'class':'lista','disabled':True}),
			'detalle_enf_operacion':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'detalle_medicamento':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'detalle_otra_enfermedad':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'otras_enfermedades': forms.CheckboxSelectMultiple(attrs={'class':'lista','disabled':True}),
		}
