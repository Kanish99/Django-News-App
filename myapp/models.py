from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField()
	address = models.CharField(max_length=256)

	class Meta:
		abstract = True


class Reporter(Person):
	position = models.CharField(max_length=64)
	
	def __str__(self):
		return self.name

class User(Person):
	phone = models.CharField(max_length=12)

	def __str__(self):
		return self.name

class Publication(models.Model):
	title = models.CharField(max_length=30)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Article(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)
	pub_date = models.DateField(default=timezone.now)
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline

	class Meta:
		ordering = ('headline', )


class Place(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class PrintingPress(models.Model):
	name = models.CharField(max_length=30)
	place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.name