from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDo


# Create your views here.
def index(request):
	todo_list = ToDo.objects.all()
	context = {'todo_list': todo_list}
	return render(request, 'todotracker/index.html', context)

def add_todo(request):
	return HttpResponse("You're adding a ToDo.")

def edit_todo(request, todo_id):
	response = "You're editing ToDo %s"
	return HttpResponse(response % todo_id)

def about(request):
	return HttpResponse("This is the about-Seite.")
