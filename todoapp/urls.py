from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_of_todos_all, name='list_of_todos'),
	url(r'^list_of_todos/active$', views.list_of_todos_active, name='list_of_todos_active'),
	url(r'^list_of_todos/completed$', views.list_of_todos_completed, name='list_of_todos_completed'),
	url(r'^(?P<id>[\d]+)/$', views.todo_detail, name='todo_detail'),
	url(r'^(?P<id>[\d]+)/delete$', views.todo_delete, name='todo_delete'),
	url(r'^(?P<id>[\d]+)/completed$', views.todo_completed, name='todo_completed'),
	url(r'^todo_add$', views.todo_add, name='todo_add'),
]