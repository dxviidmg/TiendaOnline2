from django.contrib import admin
from .models import Orden, OrdenItem

class OrderItemInline(admin.TabularInline):
	model=OrdenItem
	raw_id_fields=['producto']

class OrdenAdmin(admin.ModelAdmin):
	list_display=['id','nombre','apellidos','email','domicilio','codigo_postal','ciudad','pagado','fecha_creado','fecha_actualizado', 'empresa_envio', 'codigo_de_rastreo']
	list_filter=['pagado','fecha_creado','fecha_actualizado']
	inlines=[OrderItemInline]

admin.site.register(Orden,OrdenAdmin)