from django import forms
from .models import ToDo

class AddTodo(forms.ModelForm):
	class Meta:
		model = ToDo
		fields = ['description', 'deadline', 'progress']