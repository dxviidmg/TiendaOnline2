from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^procesando/$', views.PagoProcess.as_view(),name='processPago'),
	url(r'^hecho/$',	views.pago_done, name="donePago"),
	url(r'^cancelado/$',	views.pago_canceled,	name="canceledPago"),
]