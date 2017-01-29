# -*- coding: utf-8 -*-
from django import forms
from app.informacion.models import *
from django.contrib.admin import widgets
from app.informacion.choices import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class CodigoExpedienteForm(forms.ModelForm):
	class Meta:
		model = codigo_expediente

		fields = [
			'codigo',
		]

		labels={
			'codigo':'Codigo Expediente',
		}

		widgets={
			'codigo':forms.TextInput(attrs={'class':'form-control', 'pattern':'[0-9]{4}[-]{1}[0-9]{2}','title':'Ejemplo: 0001-16'}),
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
			'nombre_resp',
			'motivo_consulta',
			'fechaRegistro',
			'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Codigo Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Telefono',
			'genero':'Genero',
			'direccion':'Direccion',
			'nombre_resp':'Nombre del Padre o Encargado',
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creacion',
		}

		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control'}),
			'nombre_completo':forms.TextInput(attrs={'class':'form-control','title':'El nombre no puede incluir numeros o caracteres especiales','pattern':'[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ]{2,100}'}),
			'edad':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'edad_registro':forms.NumberInput(attrs={'class':'form-control','readonly':True}),

			'fecha_nac':forms.SelectDateWidget(years=range(1950,this_year,1),attrs={'class':'form-control fecha','style': 'width: 243px; display: inline-block;'}),

			'telefono':forms.TextInput(attrs={'class':'form-control', 'pattern':'[0-9]{8}','title':'Ejemplo: 77777777'}),
			'genero':forms.Select(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'nombre_resp':forms.TextInput(attrs={'class':'form-control','pattern':'[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.-]{2,100}'}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control'}),
			'fechaRegistro':forms.SelectDateWidget(years=range(this_year-1,this_year-3,-1),attrs={'class':'form-control','style': 'width: 243px; display: inline-block;'}),
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
			'nombre_resp',
			'motivo_consulta',
			'fechaRegistro',
			'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Codigo Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Telefono',
			'genero':'Genero',
			'direccion':'Direccion',
			'nombre_resp':'Nombre del Padre o Encargado',
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creacion',
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
			'nombre_resp':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'fechaRegistro':forms.DateInput(attrs={'class':'form-control','readonly':True}),
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
			'cod_expediente': 'Codigo de Expediente',
			'numero':'Numero de ficha a crear',
		}
		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'numero':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
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
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'cambio_salud' : '¿Ha habido cambio en su salud en el ultimo año?  ',
			'detalle_enf_operacion' : '¿En que consistió la enfermedad u operación?',
			'detalle_medicamento' : '¿Toma algun medicamento?',
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
			'fichas': 'Codigo Expediente y Numero de Ficha',
			'cambio_salud' : 'Cambio de Salud',
			'detalle_enf_operacion' : 'En que Consistio la enfermedad u operacion',
			'detalle_medicamento' : 'Medicamento Que ha tomado',
			'detalle_otra_enfermedad' : 'otras enfermedades',
			'otras_enfermedades': 'Tuvo alguna de estas enfermedades ',
		}	
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'cambio_salud':forms.RadioSelect(attrs={'class':'lista','disabled':True}),
			'detalle_enf_operacion':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'detalle_medicamento':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'detalle_otra_enfermedad':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'otras_enfermedades': forms.CheckboxSelectMultiple(attrs={'class':'lista','disabled':True}),
		}




		