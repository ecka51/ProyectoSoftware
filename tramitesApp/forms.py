from django import forms
from django.forms import fields
from .models import Alumno

class AlumnoForm(forms.ModelForm): 
    class Meta:
        model=Alumno
        fields='__all__'