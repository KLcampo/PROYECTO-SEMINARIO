from django.shortcuts import render
from .models import Ubicaciones, Restaurantes

# Create your views here.

def listar_Ubicaciones(self, request):
    ubicaciones = Ubicaciones.objects.filter(pk=1)
