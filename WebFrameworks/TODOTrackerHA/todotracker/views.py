from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext


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
			todo_description = request.POST.get("description", "")
			todo_deadline = request.POST.get("deadline", "")
			todo_progress = request.POST.get("progress", "")
			new_todo = ToDo(description=todo_description, deadline=todo_deadline, progress=todo_progress)
			new_todo.save()
			return render_to_response('todotracker/add-todo.html', {'todo_form': todo_form}, RequestContext(request))
	else:
		todo_form = AddTodo()
	return render_to_response('todotracker/add-todo.html', {'todo_form': todo_form})

def edit_todo(request, todo_id):
	todo = get_object_or_404(ToDo, pk=todo_id)
	context = {'todo': todo}
	return render(request, 'todotracker/edit-todo.html', context)

def about(request):
	return render(request, 'todotracker/about.html')