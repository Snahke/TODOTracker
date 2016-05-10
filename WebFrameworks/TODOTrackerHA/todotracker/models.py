from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ToDo(models.Model):
	description = models.CharField(max_length=160)
	deadline = models.DateField('Deadline')
	progress = models.IntegerField(validators=[
		MinValueValidator(0), 
		MaxValueValidator(100)
		])

	def __str__(self):
		string = self.description
		return string