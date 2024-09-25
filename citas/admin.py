from django.contrib import admin
from .models import clientes, mascotas, empleados, cargos, citas, servicios


admin.site.register(clientes)
admin.site.register(mascotas)
admin.site.register(empleados)
admin.site.register(cargos)
admin.site.register(citas)
admin.site.register(servicios)
# Register your models here.
