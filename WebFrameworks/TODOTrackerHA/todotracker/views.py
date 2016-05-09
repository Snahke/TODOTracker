from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import ToDo


# Create your views here.
def index(request):
	todo_list = ToDo.objects.all()
	context = {'todo_list': todo_list}
	return render(request, 'todotracker/index.html', context)

def add_todo(request):
	return HttpResponse("You're adding a ToDo.")

def edit_todo(request, todo_id):
	todo = get_object_or_404(ToDo, pk=todo_id)
	context = {'todo': todo}
	return render(request, 'todotracker/edit-todo.html', context)

def about(request):
	return HttpResponse("This is the about-Seite.")
