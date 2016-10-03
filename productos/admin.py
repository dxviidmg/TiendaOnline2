from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("nombre",)}

class ProductoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
# Register your models here.
