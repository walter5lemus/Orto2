# -*- coding: utf-8 -*-
from django import forms
from app.tipo_perfil.models import TipoPerfil
from app.informacion.models import fichas


class Tipo_perfilForm(forms.ModelForm):

	class Meta:
		model = TipoPerfil

		fields = [
			'fichas',
			'frontal_facial', 
			'tipoPerfiltotal', 
			'perfilTercio_inferior', 
			'tipoSonrisa', 
			'tipo_competenciaLabial',

			'tipoNariz', 
			'angulo_Naso_labial', 
			'tercio_superior', 
			'tercio_medio', 
			'tercio_inferior', 
			'tamanoSonrisa', 
			'grosorLabios',
			'tamanoLabios',  
		]

		labels = {
			'fichas': 'Numero de Ficha',

			'frontal_facial': 'Facial Frontal',
			'tipoPerfiltotal': 'Perfil total', 
			'perfilTercio_inferior': 'Perfil 1/3 inferior', 
			'tipoSonrisa': 'Tipo sonrisa', 
			'tipo_competenciaLabial': 'Competencia labial', 

			'tipoNariz': 'Tipo de nariz',
			'angulo_Naso_labial': 'Angulo naso labial',
			'tercio_superior': 'Tercio Superior',
			'tercio_medio': 'Tercio Medio',
			'tercio_inferior': 'Tercio Inferior',
			'tamanoSonrisa': 'Tamaño de Sonrisa',
			'grosorLabios': 'Grosor de labios',
			'tamanoLabios': 'Tamaño de labios',
			

		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'frontal_facial': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tipoPerfiltotal': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}), 
			'perfilTercio_inferior': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}), 
			'tipoSonrisa': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}), 
			'tipo_competenciaLabial': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}),

			'tipoNariz': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'angulo_Naso_labial': forms.NumberInput(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tercio_superior': forms.NumberInput(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tercio_medio': forms.NumberInput(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tercio_inferior':forms.NumberInput(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tamanoSonrisa':forms.NumberInput(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'grosorLabios':forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}),
			'tamanoLabios': forms.Select(attrs={'class':'form-control','min':1,'max': 2147483647}),

		}




class Tipo_perfilForm_consultar(forms.ModelForm):

	class Meta:
		model = TipoPerfil

		fields = [
			'fichas',

			'frontal_facial', 
			'tipoPerfiltotal', 
			'perfilTercio_inferior', 
			'tipoSonrisa', 
			'tipo_competenciaLabial',

			'tipoNariz', 
			'angulo_Naso_labial', 
			'tercio_superior', 
			'tercio_medio', 
			'tercio_inferior', 
			'tamanoSonrisa', 
			'grosorLabios',
			'tamanoLabios',  
		]

		labels = {
			'fichas': 'Numero de Ficha',

			'frontal_facial': 'Facial Frontal',
			'tipoPerfiltotal': 'Perfil total', 
			'perfilTercio_inferior': 'Perfil 1/3 inferior', 
			'tipoSonrisa': 'Tipo sonrisa', 
			'tipo_competenciaLabial': 'Competencia labial', 

			'tipoNariz': 'Tipo de nariz',
			'angulo_Naso_labial': 'Angulo naso labial',
			'tercio_superior': 'Tercio Superior',
			'tercio_medio': 'Tercio Medio',
			'tercio_inferior': 'Tercio Inferior',
			'tamanoSonrisa': 'Tamaño de Sonrisa',
			'grosorLabios': 'Grosor de labios',
			'tamanoLabios': 'Tamaño de labios',
			

		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'frontal_facial': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'tipoPerfiltotal': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'perfilTercio_inferior': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'tipoSonrisa': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'tipo_competenciaLabial': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),

			'tipoNariz': forms.Select(attrs={'class':'form-control','readonly':True}),
			'angulo_Naso_labial': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_superior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_medio': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_inferior':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tamanoSonrisa':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'grosorLabios':forms.Select(attrs={'class':'form-control','readonly':True}),
			'tamanoLabios': forms.Select(attrs={'class':'form-control','readonly':True}),

		}



