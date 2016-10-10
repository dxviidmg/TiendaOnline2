#-*-encoding: utf-8 -*-
from django import forms
from .models import Orden
from django.utils.translation import ugettext_lazy as _

my_default_errors = {
    'required': 'Este campo es necesario',
    'invalid': 'Introduzca un dato valido'
	}

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model=Orden
		fields=[
			'nombre',
			'apellidos',
			'email',
			'domicilio',
			'ciudad',
			'estado',
			'codigo_postal',
			]
		labels={
			'nombre':_('Tu nombre'),
			'apellidos':_('Apellidos'),
			'domicilio':_('Domicilio'),
			'ciudad':_('Ciudad'),
			'estado':_('Estado'),
			'codigo_postal':_('Codigo postal'),
			
		}
		error_messages = {
			'nombre': my_default_errors,
			'apellidos': my_default_errors,
			'email': my_default_errors,
			'domicilio': my_default_errors,
			'ciudad': my_default_errors,
			'estado': my_default_errors,
			'codigo_postal': my_default_errors,
			
		}