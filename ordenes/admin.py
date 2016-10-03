from django.contrib import admin
from .models import Orden, OrdenItem

class OrderItemInline(admin.TabularInline):
	model=OrdenItem
	raw_id_fields=['producto']

class OrdenAdmin(admin.ModelAdmin):
	list_display=['id','nombre','apellido','email','domicilio','codigo_postal','ciudad','pagado','fecha_creado','fecha_actualizado']
	list_filter=['pagado','fecha_creado','fecha_actualizado']
	inlines=[OrderItemInline]

admin.site.register(Orden,OrdenAdmin)