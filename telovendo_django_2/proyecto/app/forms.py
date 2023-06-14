from django import forms
from app.models import Proveedores



class ProveedoresForm(forms.ModelForm):
    class Meta: 
        model = Proveedores
        fields = ['nombre','razon_social','telefono','email','rut']

class FormularioLogin(forms.Form):
    #nombre del campo que se representara en la interfaz
    usuario = forms.CharField(widget=forms.TextInput())  # widget
    password=forms.CharField(widget=forms.PasswordInput())
