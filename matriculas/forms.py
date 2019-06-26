from django import forms
from .models import Matricula, Perfil, Docente, Estudiante

class Formulariomatricula(forms.ModelForm):
    class Meta:
        model=Matricula
        fields='__all__'

class Formularioperfil(forms.ModelForm):
    class Meta:
        model=Perfil
        fields='__all__'

class Formulariodocente(forms.ModelForm):
    class Meta:
        model=Docente
        fields='__all__'

class Formularioestudiante(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields='__all__'