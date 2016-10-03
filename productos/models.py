from django.db import models
from django.core.urlresolvers import reverse

class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	slug = models.SlugField()

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	marca = models.CharField(max_length=30)
	precio = models.FloatField()
	imagen = models.ImageField(upload_to='producto/', null=True, blank=True)
	slug = models.SlugField()
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('producto:detailProducto', args=[self.slug])