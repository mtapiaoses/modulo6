from django import forms
from app.models import Proveedores



class ProveedoresForm(forms.ModelForm):
    class Meta: 
        model = Proveedores
        fields = ['nombre','razon_social','telefono','email','rut']