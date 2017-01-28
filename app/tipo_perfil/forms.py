from django import forms
from app.tipo_perfil.models import TipoPerfil,PerfilTotal,FacialFrontal
from app.tipo_perfil.models import Sonrisa,PTercioInferioir, CompetenciaLabial
from app.informacion.models import fichas


class Tipo_perfilForm(forms.ModelForm):

	class Meta:
		model = TipoPerfil

		fields = [
			#'id_tipo_perfil',
			#'cod_expediente',
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
			#'id_tipo_perfil': 'Codigo',
			#'cod_expediente': 'Codigo expediente',
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
			'tamanoSonrisa': 'Tamano de Sonrisa',
			'grosorLabios': 'Grosor de labios',
			'tamanoLabios': 'Tamano de labios',
			

		}

		widgets = {
			#'id_tipo_perfil': forms.TextInput(attrs={'class':'form-control'}),
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'frontal_facial': forms.Select(attrs={'class':'form-control'}),
			'tipoPerfiltotal': forms.Select(attrs={'class':'form-control'}), 
			'perfilTercio_inferior': forms.Select(attrs={'class':'form-control'}), 
			'tipoSonrisa': forms.Select(attrs={'class':'form-control'}), 
			'tipo_competenciaLabial': forms.Select(attrs={'class':'form-control'}),

			'tipoNariz': forms.TextInput(attrs={'class':'form-control'}),
			'angulo_Naso_labial': forms.NumberInput(attrs={'class':'form-control'}),
			'tercio_superior': forms.NumberInput(attrs={'class':'form-control'}),
			'tercio_medio': forms.NumberInput(attrs={'class':'form-control'}),
			'tercio_inferior':forms.NumberInput(attrs={'class':'form-control'}),
			'tamanoSonrisa':forms.NumberInput(attrs={'class':'form-control'}),
			'grosorLabios':forms.TextInput(attrs={'class':'form-control'}),
			'tamanoLabios': forms.TextInput(attrs={'class':'form-control'}),

		}




class Tipo_perfilForm_consultar(forms.ModelForm):

	class Meta:
		model = TipoPerfil

		fields = [
			#'id_tipo_perfil',
			#'cod_expediente',
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
			#'id_tipo_perfil': 'Codigo',
			#'cod_expediente': 'Codigo expediente',
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
			'tamanoSonrisa': 'Tamano de Sonrisa',
			'grosorLabios': 'Grosor de labios',
			'tamanoLabios': 'Tamano de labios',
			

		}

		widgets = {
			#'id_tipo_perfil': forms.TextInput(attrs={'class':'form-control'}),
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'frontal_facial': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'tipoPerfiltotal': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'perfilTercio_inferior': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'tipoSonrisa': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'tipo_competenciaLabial': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),

			'tipoNariz': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'angulo_Naso_labial': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_superior': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_medio': forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tercio_inferior':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tamanoSonrisa':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'grosorLabios':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tamanoLabios': forms.TextInput(attrs={'class':'form-control','readonly':True}),

		}



