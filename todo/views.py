from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PostForm

def index(request):
    tasks = ToDoItem.objects.all()
    lists = ToDoList.objects.all()
    context = {
        'tasks':tasks,
        'lists':lists
    }
    return render(request, 'todo/index.html', context)

def task_detail(request, pk):
    task = get_object_or_404(ToDoItem, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})
    
def task_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()   
        return redirect('task_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'todo/task_create.html', {'form': form})

def task_edit(request, pk):
    post = get_object_or_404(ToDoItem, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save()
            return redirect('task_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'todo/task_edit.html', {'form':form})

def task_delete(request,pk):
    data = get_object_or_404(ToDoItem, pk=pk)
    data.delete()
    return redirect('index')

