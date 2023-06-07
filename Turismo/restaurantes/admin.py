from django.contrib import admin
from .models import Ubicaciones, Restaurantes, Formularioos

class Formularioos_Admin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')
    search_fields = ('nombre', 'correo', 'descripcion')
    list_display = ('nombre', 'correo', 'descripcion')
    ordering = ('-creado',)

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
admin.site.register(Formularioos, Formularioos_Admin)


