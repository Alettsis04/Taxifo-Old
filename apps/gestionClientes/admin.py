from django.contrib import admin
from apps.modelo.models import Persona

class AdminPersona(admin.ModelAdmin):
    list_display = ('cedula','apellidos','nombres','correo','celular')
    list_editable = ('apellidos','nombres','correo','celular')
    list_filter = ('nombres','apellidos')
    search_fields = ('nombres','apellidos','cedula')

    class Meta:
        model = Persona

admin.site.register(Persona, AdminPersona)
