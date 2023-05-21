from django.contrib import admin
from .models import Ubicaciones, Restaurantes
# Register your models here.

class Ubicaciones_Admin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')
    search_fields = ('zona', 'municipio', 'pueblo', 'accesibilidad')
    list_display = ('zona', 'municipio', 'pueblo', 'accesibilidad')
    ordering = ('-creado',)

class Restaurantes_Admin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')
    search_fields = ('nombre',)
    list_display = ('nombre',)
    ordering = ('-creado',)

admin.site.register(Ubicaciones, Ubicaciones_Admin)
admin.site.register(Restaurantes, Restaurantes_Admin)