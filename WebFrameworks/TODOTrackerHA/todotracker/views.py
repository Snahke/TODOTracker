from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import ToDo


# Create your views here.
def index(request):
	todo_list = ToDo.objects.all()
	context = {
		'todo_list': todo_list
		}
	return render(request, 'todotracker/index.html', context)


def add_todo(request):
	return render(request, 'todotracker/add-todo.html')

def edit_todo(request, todo_id):
	todo = get_object_or_404(ToDo, pk=todo_id)
	context = {'todo': todo}
	return render(request, 'todotracker/edit-todo.html', context)

def about(request):
	return render(request, 'todotracker/about.html')

def todoadd(request, todo_to_be_added):
	todo = todo_to_be_added
	todo.save()