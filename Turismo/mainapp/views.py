from django.shortcuts import render
from django.template.loader import get_template
from restaurantes.forms import PortafolioForm
import requests

# Create your views here.


def index(request):
    return render(request, 'layouts/layouts.html', {
        'title':'Inicio'
    })

def formulario(request):
    form = PortafolioForm()

    data = {'form':form}
    

    if request.method == 'POST':
        formulario = PortafolioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Datos guardados correctamente"
    return render(request, "layouts/formulario.html", data)

def galeria(request):
    return render(request, 'layouts/galeria.html', {
        'title':'galeria'
    })

def actividades(request):
    return render(request, 'layouts/actividades.html', {
        'title':'Actividades'
    })

def ubicaciones(request):
    return render(request, 'layouts/ubicaciones.html', {
        'title':'ubicaciones'
    })


