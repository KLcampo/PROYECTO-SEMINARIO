from django.urls import path
from  . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('formulario/', views.formulario, name="formulario"),
    path('galeria/', views.galeria, name="galeria"),
    path('actividades/', views.actividades, name="actividades"),
    path('ubicaciones/', views.ubicaciones, name="ubicaciones"),
]

