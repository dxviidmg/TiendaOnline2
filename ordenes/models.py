from django.db import models
from productos.models import Producto

class Orden(models.Model):

	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	email = models.EmailField()
	domicilio = models.CharField(max_length=250)
	ciudad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100, null=True, blank=True)
	codigo_postal = models.CharField(max_length=20)
	fecha_creado = models.DateTimeField(auto_now_add=True)
	fecha_actualizado = models.DateTimeField(auto_now=True)
	pagado = models.BooleanField(default=False)
	empresa_envio = models.CharField(max_length=20, null=True, blank=True)
	codigo_de_rastreo = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		ordering=('-fecha_creado',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrdenItem(models.Model):
	orden = models.ForeignKey(Orden,related_name='items')
	producto = models.ForeignKey(Producto,related_name='order_items')
	precio = models.DecimalField(max_digits=10,decimal_places=2)
	cantidad = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.precio*self.cantidad