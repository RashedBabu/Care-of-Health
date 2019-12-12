from django.db import models

# Create your models here.
class Veg(models.Model):
	Name = models.CharField(max_length=100)
	Fat = models.CharField(max_length=100)
	Protein = models.CharField(max_length=100)
	Carb = models.CharField(max_length=100)
	Fibre = models.CharField(max_length=100)
	NetCarb = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class Fruits(models.Model):
	Name = models.CharField(max_length=100)
	Fat = models.CharField(max_length=100)
	Protein = models.CharField(max_length=100)
	Carb = models.CharField(max_length=100)
	Fibre = models.CharField(max_length=100)
	NetCarb = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class Carb(models.Model):
	Name = models.CharField(max_length=100)
	Fat = models.CharField(max_length=100)
	Protein = models.CharField(max_length=100)
	Carb = models.CharField(max_length=100)
	Fibre = models.CharField(max_length=100)
	NetCarb = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class Protein(models.Model):
	Name = models.CharField(max_length=100)
	Fat = models.CharField(max_length=100)
	Protein = models.CharField(max_length=100)
	Carb = models.CharField(max_length=100)
	Fibre = models.CharField(max_length=100)
	NetCarb = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class Fat(models.Model):
	Name = models.CharField(max_length=100)
	Fat = models.CharField(max_length=100)
	Protein = models.CharField(max_length=100)
	Carb = models.CharField(max_length=100)
	Fibre = models.CharField(max_length=100)
	NetCarb = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class Others(models.Model):
	Name = models.CharField(max_length=100)
	Qty = models.CharField(max_length=100)
	Calorie = models.CharField(max_length=100)

	def __str__(self):
		return self.Name