from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class AddTodo(forms.Form):
	description = forms.CharField(max_length=160)
	deadline = forms.DateField('Deadline')
	progress = forms.IntegerField(validators=[
		MinValueValidator(0), 
		MaxValueValidator(100)
		])