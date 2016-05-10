from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddTodo
from .models import ToDo


# Create your views here.
def index(request):
	todo_list = ToDo.objects.all()
	context = {
		'todo_list': todo_list
		}
	return render(request, 'todotracker/index.html', context)


def add_todo(request):
	if request.method == 'POST':
		todo_form = AddTodo(request.POST)
		if todo_form.is_valid():
			new_todo = todo_form.save(commit=False)
			new_todo.save()
			return redirect('todotracker:index')
	else:
		todo_form = AddTodo()
	context = {'todo_form' : todo_form}
	return render(request, 'todotracker/add-todo.html', context)

def edit_todo(request, todo_id):
	todo = get_object_or_404(ToDo, pk=todo_id)
	if request.method == 'POST':
		todo_form = AddTodo(request.POST, instance=todo)
		if todo_form.is_valid():
			new_todo = todo_form.save(commit=False)
			new_todo.save()
			return redirect('todotracker:index')
	else:
		todo_form = AddTodo(instance=todo)
	context = {'todo_form' : todo_form, 'todo': todo}
	return render(request, 'todotracker/edit-todo.html', context)

def delete_todo(request, todo_id):
	todo = get_object_or_404(ToDo, pk=todo_id)
	ToDo.objects.get(pk=todo_id).delete()
	return redirect('todotracker:index')

def about(request):
	return render(request, 'todotracker/about.html', {})