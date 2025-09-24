from django import forms
from .models import Estudiante_log, Cita

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante_log
        fields = ['correo_estudiante', 'contraseña','rol']