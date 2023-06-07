from django import forms
from django.forms import ModelForm
from .models import Formularioos 

class PortafolioForm(ModelForm):
    class Meta:
        model = Formularioos
        fields = ['nombre', 'correo', 'descripcion']