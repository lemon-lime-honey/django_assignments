from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    completed = request.POST.get('completed')
    deadline = request.POST.get('deadline')
    Todo.objects.create(title=title, content=content, priority=priority, completed=completed,  deadline=deadline)
    return redirect('todos:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    completed = request.POST.get('completed')
    deadline = request.POST.get('deadline')
    todo.title = title
    todo.content = content
    todo.priority = priority
    todo.completed = completed
    todo.deadline = deadline
    todo.save()

    return redirect('todos:detail', todo.pk)


def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    completed = request.GET.get('comp')
    if completed:
        todo.completed = not todo.completed
    todo.save()

    return redirect('todos:detail', todo.pk)