from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import OrdenItem
from .forms import OrderCreateForm
from carrito.carrito import Carrito
from django.views.generic import View

class OrdenCreate(View):
	def get(sefl,request):
		cart=Carrito(request)
		form=OrderCreateForm()
		template='ordenes/ordenCreate.html'
		context={
		'cart':cart,
		'form':form
		}
		return render(request,template,context)
	def post(self,request):
		cart=Carrito(request)
		form=OrderCreateForm(request.POST)
		if form.is_valid():
			order=form.save()
			for item in cart:
				OrdenItem.objects.create(orden=order,
					producto=item['product'],
					precio=item['price'],
					cantidad=item['quantity'])
			# Borrar el carrito
			cart.clear()
			# Lanzamos la tarea asincrona
			# order_created.delay(order.id)
			# Mandamos email sin tarea asincrona
			# seteamos la orden en la sesion para paypal
			request.session['order_id']=order.id
			# redireccionamos hacia el cobro
			return redirect(reverse('payment:process'))
			# template='orders/order/created.html'
			# context={
			# 'order':order
			# }
			# return render(request,template,context)
		else:
			cart=Carrito(request)
			form=OrderCreateForm(request.POST)
			template='ordenes/ordenCreate.html'
			context={
			'cart':cart,
			'form':form
			}
		return render(request,template,context)