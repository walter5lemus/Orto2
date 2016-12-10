# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from app.AnalisisDenticionMixta.models import *

class moyersSupForm(forms.ModelForm):
	class Meta:
		model = moyers_superior

		fields = [	
			'fichas',
			'ed_izquierdo',
			'ed_derecho',		
		]

		labels = {
			'fichas': 'Numero de ficha',
			'ed_izquierdo': 'Ed Izquierdo',
			'ed_derecho': 'Ed Derecho',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
		}

class moyersSupAncForm(forms.ModelForm):
	class Meta:
		model = moyers_superior_ancho

		fields = [	
			'fichas',
			'posicion',
			'ancho_mesiodistal',		
		]

		labels = {
			'fichas': 'Numero de ficha',
			'posicion': 'Posición',
			'ancho_mesiodistal': 'Ancho Mesiodistal',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'posicion': forms.HiddenInput(attrs={'class':'form-control'}),
			'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
		}

class moyersSupForm_consultar(forms.ModelForm):
	class Meta:
		model = moyers_superior

		fields = [	
			'fichas',
			'ed_izquierdo',
			'ed_derecho',		
		]

		labels = {
			'fichas': 'Numero de ficha',
			'ed_izquierdo': 'Ed Izquierdo',
			'ed_derecho': 'Ed Derecho',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
		}

class moyersSupAncForm_consultar(forms.ModelForm):
	class Meta:
		model = moyers_superior_ancho

		fields = [	
			'fichas',
			'posicion',
			'ancho_mesiodistal',		
		]

		labels = {
			'fichas': 'Numero de ficha',
			'posicion': 'Posición',
			'ancho_mesiodistal': 'Ancho Mesiodistal',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'posicion': forms.HiddenInput(attrs={'class':'form-control'}),
			'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
		}

# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from app.AnalisisDenticionMixta.models import *


class moyersInfForm(forms.ModelForm):
    class Meta:
        model = moyers_inferior

        fields = [
            'fichas',
            'ed_izquierdo',
            'ed_derecho',
        ]

        labels = {
            'fichas': 'Numero de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ed_izquierdo': forms.NumberInput(attrs={'class': 'form-control', 'min':1,'pattern': '[0-9]{11}', 'title': 'Solo se permiten números'}),
            'ed_derecho': forms.NumberInput(attrs={'class': 'form-control', 'min':1,'pattern': '[0-9]{11}', 'title': 'Solo se permiten números'}),
        }


class moyersInfAncForm(forms.ModelForm):
    class Meta:
        model = moyers_inferior_ancho

        fields = [
            'fichas',
            'posicion',
            'ancho_mesiodistal',
        ]

        labels = {
            'fichas': 'Numero de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class': 'form-control', 'min':1,'pattern': '[0-9]{11}', 'title': 'Solo se permiten números'}),
        }


class moyersInfForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_inferior

        fields = [
            'fichas',
            'ed_izquierdo',
            'ed_derecho',
        ]

        labels = {
            'fichas': 'Numero de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ed_izquierdo': forms.NumberInput(
                attrs={'class': 'form-control','min':1, 'pattern': '[0-9]{11}', 'title': 'Solo se permiten números',
                       'readonly': True}),
            'ed_derecho': forms.NumberInput(
                attrs={'class': 'form-control','min':1, 'pattern': '[0-9]{11}', 'title': 'Solo se permiten números',
                       'readonly': True}),
        }


class moyersInfAncForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_inferior_ancho

        fields = [
            'fichas',
            'posicion',
            'ancho_mesiodistal',
        ]

        labels = {
            'fichas': 'Numero de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class': 'form-control','min':1, 'pattern': '[0-9]{11}', 'title': 'Solo se permiten números','readonly': True}),
        }
