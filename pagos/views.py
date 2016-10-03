from django.shortcuts import render
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from ordenes.models import Orden
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

class PagoProcess(View):
	def get(self,request):
		order_id=request.session.get('order_id')
		order=get_object_or_404(Orden,id=order_id)
		host=request.get_host()

		paypal_dict={
			'business':settings.PAYPAL_RECEIVER_EMAIL,
			'amount':'%.2f' % order.get_total_cost().quantize(Decimal('.01')),
			'item_name':'Order {}'.format(order.id),
			'invoice':str(order.id),
			'currency_code':'MXN',
			'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
			'return_url':'http://{}{}'.format(host,reverse('pagos:donePago')),
			'cancel_return':'http://{}{}'.format(host,reverse('pagos:canceledPago')),
		}
		form=PayPalPaymentsForm(initial=paypal_dict)
		return render(request,'pagos/processPago.html',{'order':order,'form':form})

@csrf_exempt
def pago_done(request):
	order_id=request.session.get('order_id')
	order=get_object_or_404(Orden,id=order_id)
	order.pagado = True
	order.save()
	return render(request,'pagos/donePago.html')

@csrf_exempt
def pago_canceled(request):
	return render(request,'pagos/canceledPago.html')