from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^categoria/(?P<categoria_slug>[-\w]+)/$', views.ListProductos.as_view(), name="listProductoCategoria"),
	url(r'^producto/(?P<slug>[-\w]+)/$', views.DetailProducto.as_view(), name='detailProducto'),
	url(r'^productos', views.ListProductos.as_view(),name="listProductos"),
]