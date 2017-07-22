# -*- coding: utf-8 -*
from django import forms
from app.aspectos.models import *
from app.aspectos.choices import *

class registroForm(forms.ModelForm):

	class Meta:
		model = registro

		fields = [
			'id',
			'fichas',
			'problema',
			'cuadrante',
			'pieza',
			'detalle',
		]
		labels = {
			'id': 'Id',
			'fichas': 'Ficha',
			'problema': 'Problema',
			'cuadrante': 'Cuadrante',
			'pieza': 'Pieza',
			'detalle': 'Detalle',
		}
		widgets = {
			'id': forms.HiddenInput(attrs={'class':'form-control id'}),
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'problema': forms.HiddenInput(attrs={'class':'form-control'}),
			'cuadrante': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'detalle': forms.TextInput(attrs={'class':'form-control'}),
		}

class registroForm_consultar(forms.ModelForm):

	class Meta:
		model = registro

		fields = [
			'id',
			'fichas',
			'problema',
			'cuadrante',
			'pieza',
			'detalle',
		]
		labels = {
			'id': 'Id',
			'fichas': 'Ficha',
			'problema': 'Problema',
			'cuadrante': 'Cuadrante',
			'pieza': 'Pieza',
			'detalle': 'Detalle',
		}
		widgets = {
			'id': forms.HiddenInput(attrs={'class':'form-control id','readonly':True}),
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha','readonly':True}),
			'problema': forms.HiddenInput(attrs={'class':'form-controls','readonly':True}),
			'cuadrante': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'detalle': forms.TextInput(attrs={'class':'form-control','readonly':True}),
		}

class tipo_denticionForm(forms.ModelForm):

	class Meta:
		model = tipo_denticion

		fields = [
			'fichas',
			'tipo',
		]
		labels = {
			'fichas': 'Ficha',
			'tipo': 'Tipo de dentición',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'tipo': forms.Select(attrs={'class':'form-control tipo'}),
		}

class tipo_denticionForm2(forms.ModelForm):

	class Meta:
		model = tipo_denticion

		fields = [
			'fichas',
			'tipo',
		]
		labels = {
			'fichas': 'Ficha',
			'tipo': 'Tipo de dentición',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'tipo': forms.Select(attrs={'class':'form-control tipo', 'disabled':True, 'readonly':True}),
		}

class tipo_denticionForm_consultar(forms.ModelForm):

	class Meta:
		model = tipo_denticion

		fields = [
			'fichas',
			'tipo',
		]
		labels = {
			'fichas': 'Ficha',
			'tipo': 'Tipo de dentición',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'tipo': forms.Select(attrs={'class':'form-control tipo','disabled':True,'readonly':True}),
		}

class diastemasForm(forms.ModelForm):

	class Meta:
		model = diastemas_denticion

		fields = [
			'id',
			'fichas',
			'cuad_uno',
			'pieza_uno',
			'cuad_dos',
			'pieza_dos',
		]
		labels = {
			'id': 'id',
			'fichas': 'Ficha',
			'cuad_uno': 'Cuadrante 1',
			'pieza_uno': 'Pieza 1',
			'cuad_dos': 'Cuadrante 2',
			'pieza_dos': 'Pieza 2',
		}
		widgets = {
			'id' : forms.HiddenInput(attrs={'class':'form-control id'}),
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'cuad_uno': forms.TextInput(attrs={'class':'form-control'}),
			'pieza_uno': forms.TextInput(attrs={'class':'form-control'}),
			'cuad_dos': forms.TextInput(attrs={'class':'form-control'}),
			'pieza_dos': forms.TextInput(attrs={'class':'form-control'}),
		}

class diastemasForm_consultar(forms.ModelForm):

	class Meta:
		model = diastemas_denticion

		fields = [
			'id',
			'fichas',
			'cuad_uno',
			'pieza_uno',
			'cuad_dos',
			'pieza_dos',
		]
		labels = {
			'id': 'id',
			'fichas': 'Ficha',
			'cuad_uno': 'Cuadrante 1',
			'pieza_uno': 'Pieza 1',
			'cuad_dos': 'Cuadrante 2',
			'pieza_dos': 'Pieza 2',
		}
		widgets = {
			'id' : forms.HiddenInput(attrs={'class':'form-control id','readonly':True}),
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha','readonly':True}),
			'cuad_uno': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza_uno': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'cuad_dos': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza_dos': forms.TextInput(attrs={'class':'form-control','readonly':True}),
		}


class denticionForm(forms.ModelForm):

	class Meta:
		model = denticion

		fields = [
			'fichas',
			'mal_posiciones',
			'tejido_intraorales',
			'encias',
			'frenillos',
			'lengua',
			'observaciones_generales',
		]
		labels = {
			'fichas': 'Ficha',
			'mal_posiciones': 'Mal posiciones',
			'tejido_intraorales': 'Tejidos intraorales',
			'encias': 'Encías',
			'frenillos': 'Frenillos',
			'lengua': 'Lengua',
			'observaciones_generales': 'Observaciones',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'mal_posiciones': forms.TextInput(attrs={'class':'form-control'}),
			'tejido_intraorales': forms.TextInput(attrs={'class':'form-control'}),
			'encias': forms.TextInput(attrs={'class':'form-control'}),
			'frenillos': forms.TextInput(attrs={'class':'form-control'}),
			'lengua': forms.TextInput(attrs={'class':'form-control'}),
			'observaciones_generales': forms.Textarea(attrs={'class':'form-control','rows':8}),
		}

class denticionForm_consultar(forms.ModelForm):

	class Meta:
		model = denticion

		fields = [
			'fichas',
			'mal_posiciones',
			'tejido_intraorales',
			'encias',
			'frenillos',
			'lengua',
			'observaciones_generales',
		]
		labels = {
			'fichas': 'Ficha',
			'mal_posiciones': 'Mal posiciones',
			'tejido_intraorales': 'Tejidos intraorales',
			'encias': 'Encías',
			'frenillos': 'Frenillos',
			'lengua': 'Lengua',
			'observaciones_generales': 'Observaciones',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'mal_posiciones': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tejido_intraorales': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'encias': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'frenillos': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'lengua': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'observaciones_generales': forms.Textarea(attrs={'class':'form-control','rows':3,'readonly':True}),
		}

class linea_media_facialForm(forms.ModelForm):

	class Meta:
		model = linea_media_facial

		fields = [
			'fichas',
			'mx',
			'mx_desviacion',
			'md',
			'md_desviacion',
		]
		labels = {
			'fichas': 'Ficha',
			'mx': 'Mx', 
			'mx_desviacion': 'Desviada a la',
			'md': 'Md',
			'md_desviacion': 'Desviada a la',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),			
			'mx': forms.Select(attrs={'class':'form-control'}),
			'mx_desviacion': forms.Select(attrs={'class':'form-control'}),
			'md': forms.Select(attrs={'class':'form-control'}),
			'md_desviacion': forms.Select(attrs={'class':'form-control'}),
		}

class linea_media_facialForm_consultar(forms.ModelForm):

	class Meta:
		model = linea_media_facial

		fields = [
			'fichas',
			'mx',
			'mx_desviacion',
			'md',
			'md_desviacion',
		]
		labels = {
			'fichas': 'Ficha',
			'mx': 'Mx', 
			'mx_desviacion': 'Desviada a la',
			'md': 'Md',
			'md_desviacion': 'Desviada a la',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control','readonly':True}),			
			'mx': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'mx_desviacion': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'md': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'md_desviacion': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}		

class sobremordidasForm(forms.ModelForm):

	class Meta:
		model = sobremordidas

		fields = [
			'fichas',
			'horizontal',
			'vertical',
		]
		labels = {
			'fichas': 'Ficha',
			'horizontal': 'Horizontal',
			'vertical': 'Vertical',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'horizontal': forms.Select(attrs={'class':'form-control'}),
			'vertical': forms.Select(attrs={'class':'form-control'}),
		}

class sobremordidasForm_consultar(forms.ModelForm):

	class Meta:
		model = sobremordidas

		fields = [
			'fichas',
			'horizontal',
			'vertical',
		]
		labels = {
			'fichas': 'Ficha',
			'horizontal': 'Horizontal',
			'vertical': 'Vertical',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'horizontal': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'vertical': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}

class registro_mordidasForm(forms.ModelForm):

	class Meta:
		model = registro_mordidas

		fields = [
			'id',
			'fichas',
			'cuad_superior',
			'pieza_superior',
			'cuad_inferior',
			'pieza_inferior',
		]
		labels = {
			'id': 'id',
			'fichas': 'Ficha',
			'cuad_superior': 'Cuadrante 1',
			'pieza_superior': 'Pieza 1',
			'cuad_inferior': 'Cuadrante 2',
			'pieza_inferior': 'Pieza 2',
		}
		widgets = {
			'id' : forms.HiddenInput(attrs={'class':'form-control id'}),
			'fichas': forms.HiddenInput(attrs={'class':'form-control ficha'}),
			'cuad_superior': forms.TextInput(attrs={'class':'form-control'}),
			'pieza_superior': forms.TextInput(attrs={'class':'form-control'}),
			'cuad_inferior': forms.TextInput(attrs={'class':'form-control'}),
			'pieza_inferior': forms.TextInput(attrs={'class':'form-control'}),
		}

class registro_mordidasForm_consultar(forms.ModelForm):

	class Meta:
		model = registro_mordidas

		fields = [
			'fichas',
			'cuad_superior',
			'pieza_superior',
			'cuad_inferior',
			'pieza_inferior',
		]
		labels = {
			'fichas': 'Ficha',
			'cuad_superior': 'Cuadrante 1',
			'pieza_superior': 'Pieza 1',
			'cuad_inferior': 'Cuadrante 2',
			'pieza_inferior': 'Pieza 2',
		}
		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'cuad_superior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza_superior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'cuad_inferior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'pieza_inferior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
		}

class ImagenForm(forms.ModelForm):
	class Meta:
		model = imagenes_afmp


		fields = ['fichas', 
		'nombreimagen', 
		'imagen',]

		labels = {
			'fichas': 'Numero de Ficha'	,
			'nombreimagen': 'Nombre',
			'imagen': 'Imagen',
			
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'nombreimagen':forms.TextInput(attrs={'class':'form-control'}),
			'imagen':forms.FileInput(attrs={'class':'form-control'}),
		}

class ImagenForm_consultar(forms.ModelForm):
	class Meta:
		model = imagenes_afmp


		fields = ['fichas', 
		'nombreimagen', 
		'imagen',]

		labels = {
			'fichas': 'Numero de Ficha'	,
			'nombreimagen': 'Nombre',
			'imagen': 'Imagen',
			
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'nombreimagen':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'imagen':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}


class RelacionSagitalForm(forms.ModelForm):
	class Meta:
		model = relaciones_sagitales
		
		fields = [
			'fichas',
			'molar_derecha',
			'molar_izquierda',
			'canina_derecha',
			'canina_izquierda',
			'plano_termina_recto',
			'escalon_mesial',
			'escalon_distal',
			'observaciones',
		]

		labels = {
			'fichas': 'Numero de Ficha'	,
			'molar_derecha': 'Molar Derecha',
			'molar_izquierda': 'Molar Izquierda',
			'canina_derecha': 'Canina Derecha',
			'canina_izquierda': 'Canina Izquierda',
			'plano_termina_recto': 'Plano Termina Recto',
			'escalon_mesial': 'Escalón Mesial',
			'escalon_distal': 'Escalón Distal',
			'observaciones': 'Observaciones',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'molar_derecha': forms.Select(attrs={'class':'form-control','min':0}),
			'molar_izquierda': forms.Select(attrs={'class':'form-control','min':0}),
			'canina_derecha': forms.Select(attrs={'class':'form-control','min':0}),
			'canina_izquierda': forms.Select(attrs={'class':'form-control','min':0}),
			'plano_termina_recto': forms.Select(attrs={'class':'form-control','min':0}),
			'escalon_mesial': forms.Select(attrs={'class':'form-control','min':0}),
			'escalon_distal': forms.Select(attrs={'class':'form-control','min':0}),
			'observaciones': forms.Textarea(attrs={'class':'form-control','rows':8, 'cols':3}),
		}



class RelacionSagitalForm_consultar(forms.ModelForm):
	class Meta:
		model = relaciones_sagitales
		
		fields = [
			'fichas',
			'molar_derecha',
			'molar_izquierda',
			'canina_derecha',
			'canina_izquierda',
			'plano_termina_recto',
			'escalon_mesial',
			'escalon_distal',
			'observaciones',
		]

		labels = {
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'molar_derecha': 'Molar Derecha',
			'molar_izquierda': 'Molar Izquierda',
			'canina_derecha': 'Canina Derecha',
			'canina_izquierda': 'Canina Izquierda',
			'escalon_mesial': 'Escalón Mesial',
			'escalon_distal': 'Escalón Distal',
			'observaciones': 'Observaciones',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'molar_derecha': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'molar_izquierda': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'canina_derecha': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'canina_izquierda': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'plano_termina_recto': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'escalon_mesial': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'escalon_distal': forms.Select(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'observaciones': forms.Textarea(attrs={'class':'form-control','rows':8, 'cols':3,'readonly':True}),
		}	

class FuncionMandibularForm(forms.ModelForm):
	class Meta:
		model = funcion_mandibular

		fields = [
			'fichas',
			'apertura',
			'desv_afmp_derecho',
			'desv_afmp_izquierdo',
			'signos_sintomas_atm',
		]

		labels = {
			'fichas': 'Numero de Ficha'	,
			'apertura': 'Apertura',
			'desv_afmp_derecho': 'Desviación AFMP Derecho',
			'desv_afmp_izquierdo': 'Desviación AFMP Izquierdo',
			'signos_sintomas_atm': 'Signos y Síntomas ATM',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'apertura': forms.NumberInput(attrs={'class':'form-control','min':0,'max': 2147483647}),
			'desv_afmp_derecho': forms.NumberInput(attrs={'class':'form-control','min':0,'max': 2147483647}),
			'desv_afmp_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':0,'max': 2147483647}),
			'signos_sintomas_atm': forms.Textarea(attrs={'class':'form-control'}),
		}

class FuncionMandibularForm_consultar(forms.ModelForm):
	class Meta:
		model = funcion_mandibular

		fields = [
			'fichas',
			'apertura',
			'desv_afmp_derecho',
			'desv_afmp_izquierdo',
			'signos_sintomas_atm',
		]

		labels = {
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'apertura': 'Apertura',
			'desv_afmp_derecho': 'Desviación AFMP Derecho',
			'desv_afmp_izquierdo': 'Desviación AFMP Izquierdo',
			'signos_sintomas_atm': 'Signos y Síntomas ATM',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'apertura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'desv_afmp_derecho': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'desv_afmp_izquierdo': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'signos_sintomas_atm': forms.Textarea(attrs={'class':'form-control','readonly':True}),
		}
