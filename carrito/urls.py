from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^carrito/$',
		views.DetalleCarrito.as_view(),
		name="detalleCarrito"),

	url(r'^agregar/(?P<product_id>\d+)/$',
		views.AgregaCarrito.as_view(),
		name="agregaCarrito"),

	url(r'^remove/(?P<product_id>\d+)/$',
		views.EliminaCarrito.as_view(),
		name="eliminaCarrito"),
]