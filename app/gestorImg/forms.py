# -*- coding: utf-8 -*-

from django import forms
from app.gestorImg.models import *
from django.forms.widgets import FileInput

class PacienteForm(forms.ModelForm):
	class Meta:
		model = img_paciente

		fields = ['fichas', 
		'pfacial', 
		'pfrontal',
		'psonrisa',
		'osuperior',
		'oinferior',
		'lizquierdo',
		'lderecho',
		'frontal',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'pfacial': 'Perfil Facial', 
		'pfrontal': 'Perfil Frontal',
		'psonrisa': 'Perfil Sonrisa',
		'osuperior': 'Oclusal Superior',
		'oinferior': 'Oclusal Inferior',
		'lizquierdo': 'Lateral Izquierdo',
		'lderecho': 'Lateral Derecho',
		'frontal': 'Frontal',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'pfacial':forms.FileInput(attrs={'class':'form-control'}),
			'pfrontal':forms.FileInput(attrs={'class':'form-control'}),
			'psonrisa':forms.FileInput(attrs={'class':'form-control'}),
			'osuperior':forms.FileInput(attrs={'class':'form-control'}),
			'oinferior':forms.FileInput(attrs={'class':'form-control'}),
			'lizquierdo':forms.FileInput(attrs={'class':'form-control'}),
			'lderecho':forms.FileInput(attrs={'class':'form-control'}),
			'frontal':forms.FileInput(attrs={'class':'form-control'}),
		}

class PacienteForm_consultar(forms.ModelForm):
	class Meta:
		model = img_paciente

		fields = ['fichas', 
		'pfacial', 
		'pfrontal',
		'psonrisa',
		'osuperior',
		'oinferior',
		'lizquierdo',
		'lderecho',
		'frontal',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'pfacial': 'Perfil Facial', 
		'pfrontal': 'Perfil Frontal',
		'psonrisa': 'Perfil Sonrisa',
		'osuperior': 'Oclusal Superior',
		'oinferior': 'Oclusal Inferior',
		'lizquierdo': 'Lateral Izquierdo',
		'lderecho': 'Lateral Derecho',
		'frontal': 'Frontal',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'pfacial':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'pfrontal':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'psonrisa':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'osuperior':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'oinferior':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lizquierdo':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lderecho':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'frontal':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}

class PacienteForm2(forms.ModelForm):
	class Meta:
		model = img_paciente2

		fields = ['fichas', 
		'pfacial2', 
		'pfrontal2',
		'psonrisa2',
		'osuperior2',
		'oinferior2',
		'lizquierdo2',
		'lderecho2',
		'frontal2',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'pfacial2': 'Perfil Facial', 
		'pfrontal2': 'Perfil Frontal',
		'psonrisa2': 'Perfil Sonrisa',
		'osuperior2': 'Oclusal Superior',
		'oinferior2': 'Oclusal Inferior',
		'lizquierdo2': 'Lateral Izquierdo',
		'lderecho2': 'Lateral Derecho',
		'frontal2': 'Frontal',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'pfacial2':forms.FileInput(attrs={'class':'form-control'}),
			'pfrontal2':forms.FileInput(attrs={'class':'form-control'}),
			'psonrisa2':forms.FileInput(attrs={'class':'form-control'}),
			'osuperior2':forms.FileInput(attrs={'class':'form-control'}),
			'oinferior2':forms.FileInput(attrs={'class':'form-control'}),
			'lizquierdo2':forms.FileInput(attrs={'class':'form-control'}),
			'lderecho2':forms.FileInput(attrs={'class':'form-control'}),
			'frontal2':forms.FileInput(attrs={'class':'form-control'}),
		}

class PacienteForm_consultar2(forms.ModelForm):
	class Meta:
		model = img_paciente2

		fields = ['fichas', 
		'pfacial2', 
		'pfrontal2',
		'psonrisa2',
		'osuperior2',
		'oinferior2',
		'lizquierdo2',
		'lderecho2',
		'frontal2',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'pfacial2': 'Perfil Facial', 
		'pfrontal2': 'Perfil Frontal',
		'psonrisa2': 'Perfil Sonrisa',
		'osuperior2': 'Oclusal Superior',
		'oinferior2': 'Oclusal Inferior',
		'lizquierdo2': 'Lateral Izquierdo',
		'lderecho2': 'Lateral Derecho',
		'frontal2': 'Frontal',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'pfacial2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'pfrontal2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'psonrisa2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'osuperior2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'oinferior2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lizquierdo2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lderecho2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'frontal2':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}

class RadiograficasForm(forms.ModelForm):
	class Meta:
		model = img_radiograficas

		fields = ['fichas', 
		'ipano', 
		'icefa',
		'tpano',
		'tcefa',
		'spano',
		'scefa',
		]

		labels = {
		'fichas': 'Número de Ficha', 
		'ipano': 'Radiografía Panorámica',
		'icefa': 'Radiografía Cefalométrica',
		'tpano': 'Radiografía Panorámica',
		'tcefa': 'Radiografía Cefalométrica',
		'spano': 'Radiografía Panorámica',
		'scefa': 'Radiografía Cefalométrica',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'ipano':forms.FileInput(attrs={'class':'form-control'}),
			'icefa':forms.FileInput(attrs={'class':'form-control'}),
			'tpano':forms.FileInput(attrs={'class':'form-control'}),
			'tcefa':forms.FileInput(attrs={'class':'form-control'}),
			'spano':forms.FileInput(attrs={'class':'form-control'}),
			'scefa':forms.FileInput(attrs={'class':'form-control'}),
		}

class RadiograficasForm_consultar(forms.ModelForm):
	class Meta:
		model = img_radiograficas

		fields = ['fichas', 
		'ipano', 
		'icefa',
		'tpano',
		'tcefa',
		'spano',
		'scefa',
		]

		labels = {
		'fichas': 'Número de Ficha', 
		'ipano': 'Radiografía Panorámica',
		'icefa': 'Radiografía Cefalométrica',
		'tpano': 'Radiografía Panorámica',
		'tcefa': 'Radiografía Cefalométrica',
		'spano': 'Radiografía Panorámica',
		'scefa': 'Radiografía Cefalométrica',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'ipano':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'icefa':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'tpano':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'tcefa':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'spano':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'scefa':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}

class ModeloForm(forms.ModelForm):
	class Meta:
		model = img_modelo

		fields = ['fichas', 
		'osupm',
		'oinfm',
		'lizqm',
		'frontm',
		'lderm',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'osupm': 'Oclusal Superior',
		'oinfm': 'Oclusal Inferior',
		'lizqm': 'Lateral Izquierdo',
		'frontm': 'Frontal',
		'lderm': 'Lateral Derecho',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'osupm':forms.FileInput(attrs={'class':'form-control'}),
			'oinfm':forms.FileInput(attrs={'class':'form-control'}),
			'lizqm':forms.FileInput(attrs={'class':'form-control'}),
			'frontm':forms.FileInput(attrs={'class':'form-control'}),
			'lderm':forms.FileInput(attrs={'class':'form-control'}),
		}

class ModeloForm_consultar(forms.ModelForm):
	class Meta:
		model = img_modelo

		fields = ['fichas', 
		'osupm',
		'oinfm',
		'lizqm',
		'frontm',
		'lderm',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'osupm': 'Oclusal Superior',
		'oinfm': 'Oclusal Inferior',
		'lizqm': 'Lateral Izquierdo',
		'frontm': 'Frontal',
		'lderm': 'Lateral Derecho',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'osupm':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'oinfm':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lizqm':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'frontm':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'lderm':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}

class AparatoForm(forms.ModelForm):
	class Meta:
		model = img_aparato

		fields = ['fichas', 
		'aparatof',
		'aparatol',
		'aparato',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'aparatof': 'Aparato Frontal',
		'aparatol': 'Aparato Lateral',
		'aparato': 'Aparato',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'aparatof':forms.FileInput(attrs={'class':'form-control'}),
			'aparatol':forms.FileInput(attrs={'class':'form-control'}),
			'aparato':forms.FileInput(attrs={'class':'form-control'}),
		}

class AparatoForm_consultar(forms.ModelForm):
	class Meta:
		model = img_aparato

		fields = ['fichas', 
		'aparatof',
		'aparatol',
		'aparato',
		]

		labels = {
		'fichas': 'Numero de Ficha', 
		'aparatof': 'Aparato Frontal',
		'aparatol': 'Aparato Lateral',
		'aparato': 'Aparato',
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'aparatof':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'aparatol':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
			'aparato':forms.FileInput(attrs={'class':'form-control','disabled':True,'readonly':True}),
		}