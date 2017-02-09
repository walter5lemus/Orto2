from django import forms
from app.aspMandibular.models import aspectos_mandibulares1
from app.informacion.models import fichas
from app.aspMandibular.choices import *


class aspMandibularForm(forms.ModelForm):

	class Meta:
		model = aspectos_mandibulares1

		fields = [
			#'cod_expediente',
			'fichas',

			'rama_mand_anch_izq_altura', 
			'rama_mand_anch_der_altura',
			'rama_mand_anch_simetrico',
			'rama_mand_anch_izq_aspect_observ',
			'rama_mand_anch_der_aspect_observ',

			'rama_mand_altur_izq_altura', 
			'rama_mand_altur_der_altura',
			'rama_mand_altur_simetrico',
			'rama_mand_altur_izq_aspect_observ',
			'rama_mand_altur_der_aspect_observ', 

			'cuerpo_mand_altur_izq_altura', 
			'cuerpo_mand_altur_der_altura',
			'cuerpo_mand_altur_simetrico',
			'cuerpo_mand_altur_izq_aspect_observ',
			'cuerpo_mand_altur_der_aspect_observ',

			'cuerpo_mand_long_izq_altura', 
			'cuerpo_mand_long_der_altura',
			'cuerpo_mand_long_simetrico',
			'cuerpo_mand_long_izq_aspect_observ',
			'cuerpo_mand_long_der_aspect_observ',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'rama_mand_anch_izq_altura': 'Izquierdo: (Altura)', 
			'rama_mand_anch_der_altura': 'Derecho: (Altura)',
			'rama_mand_anch_simetrico': 'Simetria:',
			'rama_mand_anch_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'rama_mand_anch_der_aspect_observ':'Aspectos observados (derecho):',

			'rama_mand_altur_izq_altura': 'Izquierdo: (Altura)', 
			'rama_mand_altur_der_altura': 'Derecho: (Altura)',
			'rama_mand_altur_simetrico': 'Simetria:',
			'rama_mand_altur_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'rama_mand_altur_der_aspect_observ': 'Aspectos observados (derecho):',

			'cuerpo_mand_altur_izq_altura': 'Izquierdo: (Altura)', 
			'cuerpo_mand_altur_der_altura': 'Derecho: (Altura)',
			'cuerpo_mand_altur_simetrico': 'Simetria:',
			'cuerpo_mand_altur_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'cuerpo_mand_altur_der_aspect_observ': 'Aspectos observados (derecho):',

			'cuerpo_mand_long_izq_altura': 'Izquierdo: (Altura)', 
			'cuerpo_mand_long_der_altura': 'Derecho: (Altura)',
			'cuerpo_mand_long_simetrico': 'Simetria:',
			'cuerpo_mand_long_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'cuerpo_mand_long_der_aspect_observ': 'Aspectos observados (derecho):',
			
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'rama_mand_anch_izq_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'rama_mand_anch_der_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'rama_mand_anch_simetrico': forms.Select(attrs={'class':'form-control'}),
			'rama_mand_anch_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
			'rama_mand_anch_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),

			'rama_mand_altur_izq_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'rama_mand_altur_der_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'rama_mand_altur_simetrico': forms.Select(attrs={'class':'form-control'}),
			'rama_mand_altur_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
			'rama_mand_altur_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),

			'cuerpo_mand_altur_izq_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'cuerpo_mand_altur_der_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'cuerpo_mand_altur_simetrico': forms.Select(attrs={'class':'form-control'}),
			'cuerpo_mand_altur_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
			'cuerpo_mand_altur_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),

			'cuerpo_mand_long_izq_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'cuerpo_mand_long_der_altura': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{2}','title':'Solo valores enteros'}),
			'cuerpo_mand_long_simetrico': forms.Select(attrs={'class':'form-control'}),
			'cuerpo_mand_long_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
			'cuerpo_mand_long_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
		}



class aspMandibularForm_consultar(forms.ModelForm):

	class Meta:
		model = aspectos_mandibulares1

		fields = [
			#'cod_expediente',
			'fichas',

			'rama_mand_anch_izq_altura', 
			'rama_mand_anch_der_altura',
			'rama_mand_anch_simetrico',
			'rama_mand_anch_izq_aspect_observ',
			'rama_mand_anch_der_aspect_observ',

			'rama_mand_altur_izq_altura', 
			'rama_mand_altur_der_altura',
			'rama_mand_altur_simetrico',
			'rama_mand_altur_izq_aspect_observ',
			'rama_mand_altur_der_aspect_observ', 

			'cuerpo_mand_altur_izq_altura', 
			'cuerpo_mand_altur_der_altura',
			'cuerpo_mand_altur_simetrico',
			'cuerpo_mand_altur_izq_aspect_observ',
			'cuerpo_mand_altur_der_aspect_observ',

			'cuerpo_mand_long_izq_altura', 
			'cuerpo_mand_long_der_altura',
			'cuerpo_mand_long_simetrico',
			'cuerpo_mand_long_izq_aspect_observ',
			'cuerpo_mand_long_der_aspect_observ',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'rama_mand_anch_izq_altura': 'Izquierdo: (Altura)', 
			'rama_mand_anch_der_altura': 'Derecho: (Altura)',
			'rama_mand_anch_simetrico': 'Simetria:',
			'rama_mand_anch_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'rama_mand_anch_der_aspect_observ':'Aspectos observados (derecho):',

			'rama_mand_altur_izq_altura': 'Izquierdo: (Altura)', 
			'rama_mand_altur_der_altura': 'Derecho: (Altura)',
			'rama_mand_altur_simetrico': 'Simetria:',
			'rama_mand_altur_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'rama_mand_altur_der_aspect_observ': 'Aspectos observados (derecho):',

			'cuerpo_mand_altur_izq_altura': 'Izquierdo: (Altura)', 
			'cuerpo_mand_altur_der_altura': 'Derecho: (Altura)',
			'cuerpo_mand_altur_simetrico': 'Simetria:',
			'cuerpo_mand_altur_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'cuerpo_mand_altur_der_aspect_observ': 'Aspectos observados (derecho):',

			'cuerpo_mand_long_izq_altura': 'Izquierdo: (Altura)', 
			'cuerpo_mand_long_der_altura': 'Derecho: (Altura)',
			'cuerpo_mand_long_simetrico': 'Simetria:',
			'cuerpo_mand_long_izq_aspect_observ': 'Aspectos observados (izquierdo)',
			'cuerpo_mand_long_der_aspect_observ': 'Aspectos observados (derecho):',
			
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'frontal_facial': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'rama_mand_anch_izq_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'rama_mand_anch_der_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'rama_mand_anch_simetrico': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'rama_mand_anch_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),
			'rama_mand_anch_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),

			'rama_mand_altur_izq_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'rama_mand_altur_der_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'rama_mand_altur_simetrico': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'rama_mand_altur_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),
			'rama_mand_altur_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),

			'cuerpo_mand_altur_izq_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'cuerpo_mand_altur_der_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'cuerpo_mand_altur_simetrico': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'cuerpo_mand_altur_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),
			'cuerpo_mand_altur_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),

			'cuerpo_mand_long_izq_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'cuerpo_mand_long_der_altura': forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'cuerpo_mand_long_simetrico': forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}), 
			'cuerpo_mand_long_izq_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),
			'cuerpo_mand_long_der_aspect_observ':forms.Textarea(attrs={'class':'form-control', 'rows':3,'readonly':True}),
		}
