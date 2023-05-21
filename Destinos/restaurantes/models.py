from django.db import models

# Create your models here.
class Ubicaciones(models.Model):
    zona = models.CharField(max_length=90, verbose_name="Zona")
    municipio = models.CharField(max_length=100, verbose_name="Municipio")
    pueblo = models.CharField(max_length=100, verbose_name="Nombre Pueblo")
    accesibilidad = models.CharField(max_length=300, verbose_name="Accesibilidad") 
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")    
    editado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualización")    
    
    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return self.zona #como se agregan mas atributos?
    
class Restaurantes(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualización")    
    ubicacion = models.ManyToManyField(Ubicaciones, verbose_name="Ubicaciones") #, blanck=True, null=True

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"

    def __str__(self):
        return self.nombre