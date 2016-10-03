"""TiendaOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from productos import urls as productosUrls
from carrito import urls as carritoUrls
from ordenes import urls as ordenesUrls
from payment import urls as paymentUrls

from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(productosUrls, namespace="productos")),
    url(r'^', include(carritoUrls, namespace="carrito")),
    url(r'^', include(ordenesUrls, namespace="ordenes")),
    url(r'^', include(paymentUrls, namespace="payment")),
    url(
            regex=r'^media/(?P<path>.*)$',
            view=serve,
            kwargs ={'document_root':settings.MEDIA_ROOT}
    ),
    ]
