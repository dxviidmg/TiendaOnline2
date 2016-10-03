from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^NuevaOrden/$', views.OrdenCreate.as_view(), name="ordenCreate"),
]