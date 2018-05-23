from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages

from .models import Todo

from .forms import TodoForm

# Create your views here.

def list_of_todos_all(request):
	todos = Todo.objects.all()
	context = {'todos': todos}
	template = 'todoapp/todo/list_of_todos.html'
	return render(request, template, context)

def list_of_todos_active(request):
	todos = Todo.objects.filter(status='active')
	context = {'todos': todos}
	template = 'todoapp/todo/list_of_todos_active.html'
	return render(request, template, context)

def list_of_todos_completed(request):
	todos = Todo.objects.filter(status='completed')
	context = {'todos': todos}
	template = 'todoapp/todo/list_of_todos_completed.html'
	return render(request, template, context)

def todo_detail(request, id):
	todo = get_object_or_404(Todo, id=id)
	template = 'todoapp/todo/todo_detail.html'
	context = {'todo': todo}
	return render(request, template, context)

def todo_delete(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	todo = get_object_or_404(Todo, id=id)
	todo.delete()
	messages.success(request, "Successfully Deleted")
	return redirect('todoapp:list_of_todos_completed')

def todo_completed(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	todo = get_object_or_404(Todo, id=id)
	todo.status = 'completed'
	todo.save()
	return redirect('todoapp:list_of_todos_completed')

def todo_add(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.created_by = request.user
			todo.save()
			return redirect('todoapp:list_of_todos')
	else:
		form = TodoForm()

	template = 'todoapp/todo/todo_add.html'
	context = {'form': form}
	return render(request, template, context)
