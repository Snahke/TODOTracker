from django.conf.urls import url

from . import views
# Create your views here.

app_name = 'todotracker'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^addtodo/', views.add_todo, name="add-todo"),
	url(r'^about/', views.about, name="about"),
	url(r'^(?P<todo_id>[0-9]+)/edittodo/$', views.edit_todo, name='edit-todo'),
]