from django import forms
from apps.modelo.models import Persona, Cliente, Agente, Barrio

class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["cedula","apellidos","nombres","genero","correo","telefono","celular"]

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["calle1","calle2","referencia1","referencia2"]

class FormularioBarrio(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ["nombre"]

class FormularioAgente(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ["funcion"]