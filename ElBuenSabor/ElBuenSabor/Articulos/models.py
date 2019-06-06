from django.db import models

class RubroArticulo(models.Model):
	denominacion = models.TextField(default='')

class Articulo(models.Model):
	denominacion = models.TextField()
	precioCompra = models.DecimalField(decimal_places=2,max_digits=7,default=0.00)
	precioVenta = models.DecimalField(decimal_places=2,max_digits=7,default=0.00)
	stockActual = models.PositiveSmallIntegerField(default=0)
	unidadDeMedida = models.TextField(default='')
	esInsumo = models.BooleanField(default = True)
	rubroArticulo = models.ForeignKey(RubroArticulo, on_delete=models.CASCADE, null= True)

class ArticuloManufacturado(models.Model):
	tiempoEstiimadoCocina = models.PositiveIntegerField(default=0)
	denominacion = models.TextField(default='')
	precioVenta = models.DecimalField(decimal_places=2,max_digits=7,default=0.00)

class ArticuloManufacturadoDetalle(models.Model):
	cantidad = models.PositiveIntegerField(default=0)
	articulo = models.ForeignKey(Articulo, on_delete = models.CASCADE, null= True )
	ArticuloManufacturado = models.ForeignKey(ArticuloManufacturado, on_delete = models.CASCADE, null= True )

class DetallePedido(models.Model):
	cantidad = models.PositiveIntegerField(default=0)
	subtotal = models.DecimalField(decimal_places=2,max_digits=7,default=0.00)
	articulo = models.ForeignKey(Articulo, on_delete = models.CASCADE, null = True)
	articuloManufacturado = models.ForeignKey(ArticuloManufacturado, on_delete = models.CASCADE, null=True)
