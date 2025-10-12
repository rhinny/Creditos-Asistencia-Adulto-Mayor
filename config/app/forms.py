from django import forms
from .models import *

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['tipo','rut','username','email', 'password']

class AdultoMForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['tipo','rut', 'username', 'email','password']
