from django.db import models

# Create your models here.
class Product(models.Model):
	id = models.AutoField(primary_key=True)
	upc12 = models.PositiveIntegerField()
	upc14 = models.PositiveIntegerField()
	brand = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name