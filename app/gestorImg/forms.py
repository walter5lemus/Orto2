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
