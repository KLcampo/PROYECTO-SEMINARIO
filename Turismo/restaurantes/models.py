from django.db import models


class Formularioos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo electronico")
    descripcion = models.CharField(max_length=500, verbose_name="descripcion")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualización") 

    class Meta:
        verbose_name = "Formularioo"
        verbose_name_plural = "Formularioos"

    def __str__(self):
        return self.nombre
    
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
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualización")    
    ubicacion = models.ManyToManyField(Ubicaciones, verbose_name="Ubicaciones") #, blanck=True, null=True

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"

    def __str__(self):
        return self.nombre