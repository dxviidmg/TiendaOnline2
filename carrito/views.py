from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.http import require_POST
# from django.utils.decorators import method_decorator
from productos.models import Producto
from .carrito import Carrito
from .forms import CartAddProductForm
from django.views.generic import View



class AgregaCarrito(View):
	def post(self,request,product_id):
		cart=Carrito(request)
		producto=get_object_or_404(Producto,id=product_id)
		form=CartAddProductForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			cart.add(product=producto,quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('carrito:detalleCarrito')

class EliminaCarrito(View):
	def get(self,request,product_id):
		cart=Carrito(request)
		product=get_object_or_404(Producto,id=product_id)
		cart.remove(product)
		return redirect('carrito:detalleCarrito')

class DetalleCarrito(View):
	def get(self,request):
		cart=Carrito(request)
		template_name="carrito/detalle.html"
		for item in cart:
			item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
		context={
		'cart':cart
		}
		return render(request,template_name,context)