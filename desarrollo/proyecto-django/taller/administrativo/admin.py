from django.contrib import admin

# Register your models here.

from administrativo.models import Propietario, Departamento

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','edad','nacionalidad')
    search_fields = ('nombre', 'apellido')

admin.site.register(Propietario,PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('costo','ncuartos','nbaños','valicuota')
    search_fields = ('costo','ncuartos')

admin.site.register(Departamento,DepartamentoAdmin)