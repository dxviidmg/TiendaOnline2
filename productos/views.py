from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View
from carrito.forms import CartAddProductForm

class ListProductos(View):
	def get(self, request, slug=None):
		template_name= "productos/listProductos.html"

		if slug:
			categoria = Categoria.objects.get(slug=slug)
			productos = Producto.objects.all().filter(categoria=categoria)
		else:
			productos = Producto.objects.all()

		categorias = Categoria.objects.all()

		form = CartAddProductForm()
		context = {
		'productos': productos,
		'categorias': categorias,
		
		'form':  form,
		}
		return render(request, template_name, context)

class DetailProducto(View):
	def get(self, request, slug):
		template_name='productos/detailProducto.html'
		producto=get_object_or_404(Producto, slug=slug)
		form = CartAddProductForm()

		context={
		'producto': producto,
		'form':  form,
		}
		return render(request, template_name, context)